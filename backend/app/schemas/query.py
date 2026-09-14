from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(min_length=1)
    top_k: int = Field(default=3, ge=1, le=10)

class SourceResponse(BaseModel):
    source: str
    chunk_index: int
    content: str

class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceResponse]
