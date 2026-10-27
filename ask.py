import anthropic
from dotenv import load_dotenv
from retrieve import find_relevant_chunk

load_dotenv()

client = anthropic.Anthropic()


def answer_question(query: str) -> dict:
    chunks = find_relevant_chunk(query)
    context = "\n\n".join(f"[{c['doc']}/{c['heading']}]\n{c['content']}"   for c in chunks)
    message  = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=800,
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}],
        system= "You are a teaching assistant for a kids’ coding course. Answer ONLY from the provided context. If the context doesn’t contain the answer, say so. Cite which document and section you used."
    )

    answer=  "".join(b.text for b in message.content if b.type == "text")

    sources=  [ {"doc": c["doc"], "heading": c["heading"]}   for c in chunks]
    return {"answer": answer, "sources": sources }



if __name__ == "__main__":
    result = answer_question("What is a function?")
    print(result["answer"])
    print("\nSources:")
    for s in result["sources"]:
        print(f"  - {s['doc']} / {s['heading']}")