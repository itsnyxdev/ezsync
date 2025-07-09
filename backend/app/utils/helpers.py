import datetime
from datetime import timedelta, datetime, timezone
from typing import Optional

import jwt
from passlib.context import CryptContext

from app.config.config import settings

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hash(password: str) -> str:
    return context.hash(password)

def password_verify(password: str, hashed_password: str) -> bool:
    return context.verify(password, hashed_password)

def generate_access_token(data: dict, expires: Optional[timedelta] = None):
    encode = data.copy()

    if expires:
        expire = datetime.now(timezone.utc) + expires
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    encode.update({"exp": expire})
    encoded_jwt = jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.SECRET_KEY_ALGORITHM)

    return encoded_jwt


def generate_refresh_token(data: dict, expires: Optional[timedelta] = None):
    encode = data.copy()

    if expires:
        expire = datetime.now(timezone.utc) + expires
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    encode.update({"exp": expire})
    encoded_jwt = jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.SECRET_KEY_ALGORITHM)

    return encoded_jwt