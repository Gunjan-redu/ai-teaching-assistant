import voyageai.error
from fastapi.testclient import TestClient
from  main import app
from retrieve import find_relevant_chunk

client = TestClient(app)

def test_ask_returns_answer_and_sources():

    res = client.post("/ask", json = {"question": "What is a function? "})

    assert res.status_code == 200
    res = res.json()
    assert "answer" in res
    assert isinstance(res["sources"] , list)


def test_alien_question_refused_with_empty_sources():
    res = client.post("/ask", json = {"question": "Who is the president of France?" })
    assert res.status_code == 200
    res = res.json()
    assert res["sources"] == []


def test_missing_question_422():
    res = client.post("/ask", json={})
    assert res.status_code == 422

def test_retrieval_with_fake_embedding(monkeypatch):

    class FakeEmbedResult:
        embeddings  = [[0.1]*1024]

    def fake_embed(*args, **kwargs):
       return FakeEmbedResult()

    import retrieve

    monkeypatch.setattr(retrieve.vo, "embed", fake_embed)

    chunks = find_relevant_chunk("anything")
    assert len(chunks) == 3
    assert  "content" in chunks[0]

def test_voyage_rate_limit_returns_429(monkeypatch):
    def fake_embed_that_fails(*args, **kwargs):
        raise voyageai.error.RateLimitError("too fast")


    import retrieve
    monkeypatch.setattr(retrieve.vo, "embed", fake_embed_that_fails)

    res = client.post("/ask", json={"question": "anything"})
    assert res.status_code == 429
    assert "rate-limited" in res.json()["detail"]