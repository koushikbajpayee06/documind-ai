from typing import Any

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    number_of_results: int = Field(
        default=4,
        ge=1,
        le=10,
    )


class SearchResult(BaseModel):
    content: str
    metadata: dict[str, Any]


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]