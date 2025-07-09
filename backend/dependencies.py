from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.config.database import mariadb_session_local

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_mariadb() -> Session:
    db = mariadb_session_local()
    try:
        yield db
    finally:
        db.close()