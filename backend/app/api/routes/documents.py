import logging
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.config import settings
from app.schemas.document import DocumentUploadResponse
from app.services.document_service import create_chunks, extract_text
from app.services.storage_service import save_uploaded_file


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    file: UploadFile = File(...),
) -> DocumentUploadResponse:
    try:
        saved_file = await save_uploaded_file(file)

        stored_path = (
            Path(settings.upload_dir)
            / saved_file["stored_filename"]
        )

        extracted_text = extract_text(stored_path)

        chunks = create_chunks(
            text=extracted_text,
            source=saved_file["original_filename"],
        )

        return DocumentUploadResponse(
            message="Document uploaded and processed successfully",
            character_count=len(extracted_text),
            chunk_count=len(chunks),
            **saved_file,
        )

    except (ValueError, FileNotFoundError) as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    except Exception as error:
        logger.exception(
            "Unexpected error while uploading and processing document"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload and process document",
        ) from error