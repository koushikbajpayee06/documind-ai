import logging

from fastapi import APIRouter, HTTPException, status

from app.schemas.search import (
    SearchRequest,
    SearchResponse,
    SearchResult,
)
from app.services.vector_store import search_documents


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/search",
    tags=["Search"],
)


@router.post(
    "/semantic",
    response_model=SearchResponse,
)
async def semantic_search(
    request: SearchRequest,
) -> SearchResponse:
    try:
        document_score_pairs = search_documents(
            query=request.query,
            number_of_results=request.number_of_results,
        )

        results = [
            SearchResult(
                content=document.page_content,
                metadata=document.metadata,
                distance=distance,
            )
            for document,distance in document_score_pairs
        ]

        return SearchResponse(
            query=request.query,
            results=results,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    except Exception as error:
        logger.exception(
            "Unexpected error during semantic search"
        )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Semantic search failed",
        ) from error