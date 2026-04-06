Claims Document Analyzer

Overview
Claims Document Analyzer is an AI-powered application built to simplify how users read and analyze claims-related PDF documents.

Instead of manually reviewing long files, the system:

* Extracts key information
* Summarizes content
* Enables users to interact using natural language questions

This project demonstrates how NLP, embeddings, and vector search can be combined to create a practical document intelligence solution.

---

Problem Statement

In domains like insurance and healthcare, claim documents contain a lot of unstructured data such as:

* Claimant details
* Policy information
* Medical records and diagnosis
* Dates and financial values

Reading these documents manually is time-consuming and inefficient.

This project helps convert raw text into searchable and structured insights, reducing manual effort.

---

What This Application Does

After uploading a PDF, the system performs the following steps:

1. Extracts text from the document
2. Splits text into smaller chunks
3. Converts chunks into vector embeddings
4. Stores embeddings in FAISS index
5. Extracts named entities using NLP
6. Generates a short summary
7. Allows natural language querying

This makes the document easier to explore and understand.

---

Key Features

* Upload and process PDF documents
* Automatic text extraction and chunking
* Semantic search using embeddings
* Fast retrieval with FAISS
* Named Entity Recognition (NER)
* Quick summary generation
* Ask questions in natural language

---

Example Queries

Users can ask:

* What is the claim amount?
* Who is the claimant?
* What diagnosis is mentioned?
* What are the key dates?

The system returns the most relevant information from the document.

---

Project Structure

claims-document-analyzer/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│
│   ├── api/
│   │   └── routes.py
│
│   ├── core/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   ├── ner.py
│   │   ├── summarizer.py
│   │   └── rag_chain.py
│
│   └── data/
│       ├── uploads/
│       └── faiss_index/
│
├── run.py
├── requirements.txt
├── .env.example
└── venv/

---

How It Works

The workflow is simple and efficient:

1. Upload a PDF using the API
2. Text is extracted from the document
3. Content is split into chunks
4. Each chunk is converted into embeddings
5. Stored in FAISS vector index

User can:

* Generate a summary
* Extract entities
* Ask questions

---

Tech Stack

Python
FastAPI
Uvicorn
LangChain
FAISS
Sentence Transformers
SpaCy
PyPDF
Pydantic

---

How to Run

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python run.py

Open Swagger UI:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

API Endpoints

/upload → Upload and process document
/summary → Get summary
/entities → Extract entities
/query → Ask questions

---

Current Scope (MVP)

PDF processing pipeline
Semantic search with FAISS
Entity extraction
Summary generation
Query-based retrieval

---

Future Enhancements

OCR support for scanned PDFs
Claims-specific field extraction
Frontend UI (React / Streamlit)
Multi-document search
Database integration

---

Author Name :- Kiran Teja
