import logging

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.document import DocumentUploadResponse
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

        return DocumentUploadResponse(
            message="Document uploaded successfully",
            **saved_file,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    except Exception as error:
        logger.exception("Unexpected error while uploading document")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),  # শুধু development debugging-এর জন্য
        ) from error