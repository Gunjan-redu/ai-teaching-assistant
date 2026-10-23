from dotenv import load_dotenv
import voyageai


load_dotenv()

vo = voyageai.Client()

result = vo.embed(["A variable is like a container"], model='voyage-code-4')

vec = result.embeddings[0]
print(len(vec))
print(vec[0:5])
print(result.total_tokens)
