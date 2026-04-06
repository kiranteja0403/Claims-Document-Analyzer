import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Claims Document Analyzer")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
LLM_MODEL = os.getenv("LLM_MODEL", "google/flan-t5-base")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "app/data/uploads")
FAISS_DIR = os.getenv("FAISS_DIR", "app/data/faiss_index")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(FAISS_DIR, exist_ok=True)