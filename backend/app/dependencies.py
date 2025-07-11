from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.utils import decode_jwt_token, init_mariadb
from app.models import User, Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_authenticated_user(token: str = Depends(oauth2_scheme), db_session: AsyncSession = Depends(init_mariadb)):
    authentication_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    jwt_payload = decode_jwt_token(token)
    if jwt_payload is None:
        raise authentication_error

    username: str | None = jwt_payload.get("sub")
    jwt_id: str | None = jwt_payload.get("jwt_id")

    if username is None or jwt_id is None:
        raise authentication_error

    async with db_session as session:
        token_query_result = await session.execute(
            select(Token).where(Token.jwt_id == jwt_id)
        )
        token_instance = token_query_result.scalars().first()

        if not token_instance or token_instance.is_revoked:
            raise authentication_error

        user_query_result = await session.execute(select(User).where(User.username == username))
        user_instance = user_query_result.scalars().first()

        if user_instance is None:
            raise authentication_error

        return user_instance
