from sqlalchemy import BigInteger, Identity, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base, HasTimestamps


class User(Base, HasTimestamps):
    __tablename__ = "users"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mariadb_engine": "InnoDB",
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_unicode_ci",
    }

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    username: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)

    tokens = relationship("Token", back_populates="user", cascade="all, delete-orphan")
