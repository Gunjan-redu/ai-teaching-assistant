
from  ask import answer_question

while True:

    q = input("Ask (or quit): ")

    if q.lower() in ("quit", "exit"):
        break
    result = answer_question(q)
    print("\n" + result["answer"])

    print("\nSources: " + ", ".join(f"{s['doc']}/{s['heading']}" for s in result["sources"]))