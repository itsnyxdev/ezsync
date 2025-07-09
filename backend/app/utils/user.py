from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate
from app.utils import password_hash


def get_user_by_username_email(db: Session, email: str, username: str):
    return db.query(User).filter(User.email == email or User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user