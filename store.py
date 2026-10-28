from dotenv import load_dotenv
from chunker import chunk_documents
import psycopg2
import voyageai


load_dotenv()

docs = ["documents/01_variables.md", "documents/02_loops.md", "documents/03_functions.md"]

conn = psycopg2.connect(host="localhost", port =5433, dbname = "teaching_assistant", user="postgres", password = "secret")

cur = conn.cursor()

if __name__ == "__main__":
    all_chunks  = []
    for d in docs:
        doc_chunks = chunk_documents(d)
        cur.execute("DELETE FROM chunks WHERE document_name = %s", (d,))
        all_chunks.extend(doc_chunks)

    print(f"{len(all_chunks)} chunks")

    vo = voyageai.Client()
    texts = [c["text"]   for c in all_chunks]
    result = vo.embed(texts, model="voyage-code-4", input_type="document")
    print(f"embedded, {result.total_tokens} tokens")



    for chunk, vec in zip(all_chunks, result.embeddings):
        cur.execute(
            """INSERT INTO chunks (document_name, heading, chunk_index, content, embedding)
                VALUES (%s, %s, %s, %s, %s)
            """,
            (chunk["doc"], chunk["heading"], chunk["chunk_index"], chunk["text"], str(vec)),
        )
    conn.commit()
    cur.close()
    conn.close()
    print("stored")
