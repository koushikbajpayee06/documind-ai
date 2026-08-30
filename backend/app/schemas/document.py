from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    message: str
    original_filename: str
    stored_filename: str
    content_type: str
    size_bytes: int