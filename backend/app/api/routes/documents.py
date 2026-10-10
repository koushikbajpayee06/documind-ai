import logging
from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile, status
from app.config import settings
from app.schemas.document import DocumentUploadResponse
from app.services.document_service import create_chunks, load_documents
from app.services.storage_service import save_uploaded_file
from app.services.vector_store import add_documents_to_vector_store


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

        documents = load_documents(
            file_path=stored_path,
            source=saved_file["original_filename"],
        )

        chunks = create_chunks(
            documents=documents,
        )

        document_ids = add_documents_to_vector_store(chunks)

        return DocumentUploadResponse(
            message="Document uploaded, processed, and indexed successfully",
            character_count=sum(
                len(document.page_content)
                for document in documents
            ),
            chunk_count=len(document_ids),
            **saved_file,
        )
    except (ValueError, FileNotFoundError) as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    except Exception as error:
        logger.exception(
            "Unexpected error while uploading, processing, and indexing document"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to upload, process, and index document",
        ) from error