import anthropic
from dotenv import load_dotenv
from retrieve import find_relevant_chunk

load_dotenv()

client = anthropic.Anthropic()

query = "What is a function?"

chunks = find_relevant_chunk(query)

[   for c in chunks]

print(chunks)
'''
message  = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=800,
    messages= [{"role": "user", "content": query}],
    system= "You are a teaching assistant for a kids’ coding course. Answer ONLY from the provided context. If the context doesn’t contain the answer, say so. Cite which document and section you used."
)

print(message)

'''