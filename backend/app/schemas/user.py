from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict
from app.utils import UsernameStr, PasswordStr


class UserCreate(BaseModel):
    email: EmailStr
    username: UsernameStr
    password: PasswordStr
    full_name: Optional[str] = None

class UserAsResponse(BaseModel):
    email: EmailStr
    username: UsernameStr
    full_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)