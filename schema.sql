CREATE TABLE chunks(
     id SERIAL PRIMARY KEY,
     document_name TEXT NOT NULL,
     heading TEXT,
     chunk_index INTEGER NOT NULL,
     content TEXT NOT NULL,
     embedding vector(1536)     -- needs pgvector extension; dimension TBD by model
     created_at TIMESTAMP DEFAULT now()

)