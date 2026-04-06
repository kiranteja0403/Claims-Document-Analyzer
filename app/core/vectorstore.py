from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embedding_model

def build_and_save_vectorstore(chunks, save_path: str):
    embeddings = get_embedding_model()
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    vectorstore.save_local(save_path)

def load_vectorstore(load_path: str):
    embeddings = get_embedding_model()
    return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)