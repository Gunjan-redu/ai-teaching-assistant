import voyageai.error
from fastapi.testclient import TestClient
from  main import app
from retrieve import find_relevant_chunk

client = TestClient(app)

def test_ask_returns_answer_and_sources(monkeypatch):
    class FakeTextBlock:
        type = "text"
        text = "A while loop repeats while a condition is true."

    class FakeMessage:
        content = [FakeTextBlock()]

    def fake_create(*args, **kwargs):
        return FakeMessage()

    class FakeEmbedding:
        embeddings = [[0.1] * 1024]

    def fake_embed(*args, **kwargs):
        return FakeEmbedding()

    import retrieve
    monkeypatch.setattr(retrieve.vo, "embed", fake_embed)

    import ask
    monkeypatch.setattr(ask.client.messages, "create", fake_create)

    res = client.post("/ask", json = {"question": "What is a function? "})

    assert res.status_code == 200
    res = res.json()
    assert "answer" in res
    assert isinstance(res["sources"] , list)


def test_alien_question_refused_with_empty_sources(monkeypatch):

    class FakeEmbedding:
        embeddings =  [[0.9] * 1024]

    def get_fake_embedings(*args, **kwargs):
        return FakeEmbedding()

    import retrieve

    monkeypatch.setattr(retrieve.vo, "embed", get_fake_embedings)

    res = client.post("/ask", json={"question": "anything"})
    assert res.status_code == 200
    data = res.json()
    assert data["sources"] == []


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