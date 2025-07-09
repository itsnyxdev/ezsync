from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum, BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import MariaDBBase, TimestampMixin


class User(MariaDBBase, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(16), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)
    password: Mapped[str] = mapped_column(Text, index=True, nullable=False)

class ExpiredToken(MariaDBBase):
    __tablename__ = "expired_tokens"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    jwt_id: Mapped[str] = mapped_column(Text, index=True, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(BigInteger, index=True, nullable=False)
