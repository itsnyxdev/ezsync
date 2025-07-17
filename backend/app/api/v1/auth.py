from fastapi import APIRouter, Depends, HTTPException, status, Response, Body, Request
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy import or_, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from starlette.responses import JSONResponse

from app.utils import (
    init_mariadb,
    get_db_session,
    generate_password_hash,
    decode_jwt_token,
    is_password_valid,
    generate_refresh_token,
    generate_access_token
)

from app.models import User, Token
from app.schemas import UserCreate, UserAsResponse
from app.schemas import TokenSchema
from app.dependencies import get_authenticated_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserAsResponse, status_code=status.HTTP_201_CREATED, response_class=JSONResponse)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db_session)):

    query = select(User).where(or_(User.username == user_in.username, User.email == user_in.email))
    existing_user = await db.scalar(query)

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = generate_password_hash(user_in.password)
    new_user = User(
        username=user_in.username,
        email=user_in.email,
        password=hashed_password,
        full_name=user_in.full_name
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


@router.post("/login", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.username == form_data.username))
    user = result.scalars().first()

    if not user or not is_password_valid(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token, access_jti = generate_access_token({"sub": user.username, "type": "access"})
    refresh_token, refresh_jti = generate_refresh_token({"sub": user.username, "type": "refresh"})

    access_token_record = Token(jwt_id=access_jti, user_id=user.id)
    refresh_token_record = Token(jwt_id=refresh_jti, user_id=user.id)

    db.add_all([access_token_record, refresh_token_record])
    await db.commit()

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(current_user: User = Depends(get_authenticated_user), db: AsyncSession = Depends(get_db_session)):
    stmt = (
        update(Token)
        .where(Token.user_id == current_user.id, Token.is_revoked == False)
        .values(is_revoked=True)
    )

    await db.execute(stmt)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/refresh", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(..., embed=True), db: AsyncSession = Depends(get_db_session)):
    decoded_token = decode_jwt_token(refresh_token)

    if not decoded_token or decoded_token.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    username = decoded_token.get("sub")
    refresh_jti = decoded_token.get("jti")

    token_record = await db.scalar(select(Token).where(Token.jwt_id == refresh_jti))

    if not token_record:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    if token_record.is_revoked:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token has been revoked",
        )

    new_access_token, new_access_jti = generate_access_token(
        {"sub": username, "type": "access"}
    )
    new_refresh_token, new_refresh_jti = generate_refresh_token(
        {"sub": username, "type": "refresh"}
    )

    new_access_token_record = Token(jwt_id=new_access_jti, user_id=token_record.user_id)
    new_refresh_token_record = Token(
        jwt_id=new_refresh_jti, user_id=token_record.user_id
    )

    db.add_all([new_access_token_record, new_refresh_token_record])
    await db.commit()

    response_data = {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }

    return response_data



@router.get("/me", response_model=UserAsResponse)
async def read_users_me(current_user: User = Depends(get_authenticated_user)):
    return current_user
