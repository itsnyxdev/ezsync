from sqlalchemy import Identity, Text, BigInteger, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from app.models import Base, HasTimestamps


class Token(Base, HasTimestamps):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    jwt_id: Mapped[str] = mapped_column(Text, unique=True, index=True, nullable=False)
    user_id: Mapped[str] = mapped_column(BigInteger, index=True, nullable=False)
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False)