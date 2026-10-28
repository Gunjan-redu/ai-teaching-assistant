from fastapi.testclient import TestClient
from  main import app

client = TestClient(app)

def test_ask_returns_answer_and_sources():

    res = client.post("/ask", json = {"question": "What is a function? "})

    assert res.status_code == 200
    res = res.json()
    assert "answer" in res
    assert isinstance(res["sources"] , list)
