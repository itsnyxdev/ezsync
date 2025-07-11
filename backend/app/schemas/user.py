from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    full_name: Optional[str] = None

class UserAsResponse(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)