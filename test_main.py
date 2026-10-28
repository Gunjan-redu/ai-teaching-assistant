from fastapi.testclient import TestClient
from  main import app

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
