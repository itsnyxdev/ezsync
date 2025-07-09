from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import UserCreate
from app.utils import get_user_by_email, create_user
from app.utils.user import get_user_by_username_email
from dependencies import get_mariadb

router = APIRouter(prefix="/api/auth")

@router.post("/login")
async def login():
    pass

@router.get("/test")
async def test():
    return {"message": "Test endpoint"}


@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_mariadb)):
    db_user = get_user_by_username_email(db, email=user.email, username=user.username)
    if db_user:
        return HTTPException(status_code=400, detail="Email already registered.")
    return create_user(db, user=user)