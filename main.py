from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse

from ask import answer_question
import anthropic
import voyageai

app = FastAPI()

class AskIn(BaseModel):
    question : str


class Source(BaseModel):
    doc: str
    heading: str

class AskOut(BaseModel):
    answer: str
    sources: list[Source]


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/ask")
def ask(body:AskIn)-> AskOut:
    try:
        answer = answer_question(body.question)
    except anthropic.APITimeoutError:
        raise HTTPException(status_code= 504, detail="Anthropic API timed out")
    except anthropic.APIError:
        raise HTTPException(status_code= 502, detail="Anthropic API Error")
    except voyageai.error.RateLimitError:
        raise HTTPException(status_code=429, detail="Embedding service rate-limited — try again in a few seconds")
    except voyageai.error.VoyageError:
        raise HTTPException(status_code=502, detail="Embedding service error")
    return answer