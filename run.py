from app.services.ingesion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents
docs = chunk_documents(load_file(Path("data/sample_kb/company_it_handbook.md")))

add_documents(docs)
