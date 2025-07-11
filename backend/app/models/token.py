from sqlalchemy import Identity, Text, BigInteger, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models import Base, HasTimestamps


class Token(Base, HasTimestamps):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    jwt_id: Mapped[str] = mapped_column(Text, unique=True, index=True, nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), index=True, nullable=False)
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False)

    user = relationship("User", back_populates="tokens")