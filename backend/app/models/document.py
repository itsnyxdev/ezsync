import datetime
from enum import Enum, StrEnum
from typing import List, Any

from beanie import Document, PydanticObjectId
from bson import Timestamp, ObjectId
from pydantic import Field

from app.utils.types import LevelType


class Category(Document):
    name: str = Field(alias="name")
    created_at: float =  Field(alias="createdAt")

    class Settings:
        name = "categories"

class Job(Document):
    slug: str
    link: str
    title: str = Field(alias="title")
    location: Any
    company: str = Field(alias="company")
    levels: List[LevelType] = Field(alias="levelType")
    modified_at: datetime.datetime = Field(alias="modifiedAt")
    category_id: PydanticObjectId = Field(alias="categoryId")

    class Settings:
        name = "jobs"


