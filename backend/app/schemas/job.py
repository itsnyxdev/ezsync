from datetime import datetime
from typing import Any, List
from beanie import PydanticObjectId
from pydantic import BaseModel

from app.utils.types import LevelType


class CategoryResponse(BaseModel):
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