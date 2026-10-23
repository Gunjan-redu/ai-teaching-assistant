CREATE TABLE chunks(
     id SERIAL PRIMARY KEY,
     document_name TEXT NOT NULL,
     heading TEXT,
     chunk_index INTEGER NOT NULL,
     content TEXT NOT NULL,
     embedding vector(1024),  -- voyage-code-4 embeddings, 1024 dims
     created_at TIMESTAMP DEFAULT now()

)