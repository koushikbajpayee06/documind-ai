from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.config import settings


ALLOWED_EXTENSIONS = {".pdf", ".txt", ".md"}


async def save_uploaded_file(file: UploadFile) -> dict:
    if not file.filename:
        raise ValueError("Filename is required")

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Unsupported file type. Only PDF, TXT, and Markdown files are allowed."
        )

    file_content = await file.read()
    max_size_bytes = settings.max_upload_size_mb * 1024 * 1024

    if not file_content:
        raise ValueError("The uploaded file is empty")

    if len(file_content) > max_size_bytes:
        raise ValueError(
            f"File size exceeds the {settings.max_upload_size_mb} MB limit"
        )

    upload_directory = Path(settings.upload_dir)
    upload_directory.mkdir(parents=True, exist_ok=True)

    stored_filename = f"{uuid4()}{extension}"
    destination = upload_directory / stored_filename

    destination.write_bytes(file_content)

    await file.close()

    return {
        "original_filename": file.filename,
        "stored_filename": stored_filename,
        "content_type": file.content_type or "application/octet-stream",
        "size_bytes": len(file_content),
    }