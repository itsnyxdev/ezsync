from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    username: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True