from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from app.utils import decode_jwt_token, init_mariadb
from app.models import User, Token
from app.utils.database import get_db_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", scheme_name="JWT")


async def get_authenticated_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db_session)):
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
            detail="Invalid token type, expected access token"
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
