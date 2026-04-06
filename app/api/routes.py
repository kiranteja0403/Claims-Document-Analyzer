import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas import QueryRequest, QueryResponse, SummaryResponse, EntityResponse, UploadResponse
from app.config import UPLOAD_DIR, FAISS_DIR
from app.core.loader import extract_text_from_pdf
from app.core.chunker import create_chunks
from app.core.vectorstore import build_and_save_vectorstore, load_vectorstore
from app.core.ner import extract_entities
from app.core.summarizer import generate_summary
from app.core.rag_chain import ask_question

router = APIRouter()

DOCUMENT_CACHE = {
    "text": "",
    "chunks": []
}

@router.get("/")
def home():
    return {"message": "Claims Document Analyzer API is running"}

@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    if not text.strip():
        raise HTTPException(status_code=400, detail="No text extracted from PDF")

    chunks = create_chunks(text)
    build_and_save_vectorstore(chunks, FAISS_DIR)

    DOCUMENT_CACHE["text"] = text
    DOCUMENT_CACHE["chunks"] = chunks

    return UploadResponse(filename=file.filename, message="Document uploaded and indexed successfully")

@router.get("/summary", response_model=SummaryResponse)
def get_summary():
    if not DOCUMENT_CACHE["text"]:
        raise HTTPException(status_code=400, detail="No document uploaded yet")

    summary = generate_summary(DOCUMENT_CACHE["text"])
    return SummaryResponse(summary=summary)

@router.get("/entities", response_model=EntityResponse)
def get_entities():
    if not DOCUMENT_CACHE["text"]:
        raise HTTPException(status_code=400, detail="No document uploaded yet")

    entities = extract_entities(DOCUMENT_CACHE["text"])
    return EntityResponse(entities=entities)

@router.post("/query", response_model=QueryResponse)
def query_document(request: QueryRequest):
    if not DOCUMENT_CACHE["text"]:
        raise HTTPException(status_code=400, detail="No document uploaded yet")

    vectorstore = load_vectorstore(FAISS_DIR)
    answer = ask_question(request.question, vectorstore)

    return QueryResponse(question=request.question, answer=answer)

