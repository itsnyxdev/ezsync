from datetime import datetime
from typing import Any, List, Optional
from beanie import PydanticObjectId
from pydantic import BaseModel, ConfigDict, Field

from app.utils.types import LevelType


class CategoryResponse(BaseModel):
    id: PydanticObjectId
    name: str
    created_at: datetime


class JobResponse(BaseModel):
    slug: str
    link: str
    title: str
    location: Any
    company: str
    levels: List[LevelType]
    modified_at: datetime
    category_id: PydanticObjectId

    model_config = ConfigDict(
        json_encoders={PydanticObjectId: str, datetime: lambda v: v.isoformat()}
    )


class PaginationMeta(BaseModel):
    currentPage: int
    totalPages: int
    totalItems: int
    itemsPerPage: int
    hasNextPage: bool
    hasPrevPage: bool

class JobsResponse(BaseModel):
    data: List[JobResponse]
    meta: PaginationMeta


class JobsFilterRequest(BaseModel):
    page: int = Field(1, ge=1)
    limit: int = Field(10, ge=1, le=100)
    category_id: Optional[PydanticObjectId] = Field(None)
    level: Optional[LevelType] = Field(None)
    location: Optional[str] = Field(None)
    search: Optional[str] = Field(None, max_length=100)