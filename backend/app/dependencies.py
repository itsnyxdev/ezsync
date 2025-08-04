from datetime import timezone, datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from app.utils import decode_jwt_token
from app.models import User, Token
from app.utils.database import get_db_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", scheme_name="JWT")


async def get_authenticated_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db_session)) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


    payload = decode_jwt_token(token)
    if payload is None:
        raise credentials_exception

    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token type, expected access token",
        )

    jti = payload.get("jti")
    username = payload.get("sub")
    exp = payload.get("exp")

    if not jti or not username:
        raise credentials_exception

    if exp and datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_query = select(Token).where(Token.jwt_id == jti, Token.is_revoked == False)
    token_record = await db.scalar(token_query)

    if not token_record:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token not found or has been revoked",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_query = select(User).where(User.id == token_record.user_id)
    user = await db.scalar(user_query)

    if not user:
        raise credentials_exception

    return user


async def get_authenticated_user_with_tokens(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db_session)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_jwt_token(token)
    if payload is None:
        raise credentials_exception

    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token type, expected access token",
        )

    jti = payload.get("jti")
    if jti is None:
        raise credentials_exception

    query = (
        select(User)
        .join(Token, User.id == Token.user_id)
        .where(Token.jwt_id == jti, Token.is_revoked == False)
        .options(joinedload(User.tokens))
    )

    result = await db.execute(query)
    user = result.scalars().first()

    if user is None:
        raise credentials_exception

    return user