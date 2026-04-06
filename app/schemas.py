from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    answer: str

class SummaryResponse(BaseModel):
    summary: str

class EntityResponse(BaseModel):
    entities: list

class UploadResponse(BaseModel):
    filename: str
    message: str