import voyageai
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

vo = voyageai.Client()

conn = psycopg2.connect(host=os.environ["DB_HOST"], port =os.environ["DB_Port"], dbname = os.environ["DB_NAME"], user=os.environ["DB_USER"], password = os.environ["DB_PASSWORD"])
cur = conn.cursor()

def find_relevant_chunk(question: str, top_k=3) -> list[dict]:
   result=  vo.embed([question], model='voyage-code-4', input_type="query")
   emb_question =  str(result.embeddings[0])
   cur.execute(
      """
         SELECT document_name, heading, content, 
            embedding <=> %s::vector AS distance
         FROM chunks
         ORDER BY distance
         LIMIT %s;
      """,
      (emb_question, top_k)
   )

   rows = cur.fetchall()
   return [
      {"doc": r[0], "heading": r[1], "content": r[2], "distance": r[3]}
      for r in rows
   ]


if __name__ == "__main__":
    for q in ["what is a dictionary?", "how do I repeat code?", "what is a while loop?"]:
        print(f"\n=== {q}")
        for c in find_relevant_chunk(q):

            print(f"  [{c['distance']:.3f}] {c['doc']} / {c['heading']}: {c['content'][:60]!r}")