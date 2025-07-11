import uuid
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.config import settings


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def is_password_valid(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def generate_password_hash(password: str) -> str:
    return password_context.hash(password)


def generate_jwt_token(payload_data: dict, expiration_duration: timedelta) -> tuple[str, str]:
    token_payload = payload_data.copy()
    expiration_time = datetime.now(timezone.utc) + expiration_duration
    jwt_id = str(uuid.uuid4())
    token_payload.update({"exp": expiration_time, "jti": jwt_id})
    jwt_token = jwt.encode(token_payload, settings.secret_key, algorithm=settings.algorithm)
    return jwt_token, jwt_id


def generate_access_token(payload_data: dict) -> tuple[str, str]:
    access_token_expiration = timedelta(minutes=settings.access_token_expire_minutes)
    return generate_jwt_token(payload_data, access_token_expiration)


def generate_refresh_token(payload_data: dict) -> tuple[str, str]:
    refresh_token_expiration = timedelta(days=settings.refresh_token_expire_days)
    return generate_jwt_token(payload_data, refresh_token_expiration)


def decode_jwt_token(token: str) -> dict | None:
    try:
        decoded_payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return decoded_payload
    except JWTError:
        return None
