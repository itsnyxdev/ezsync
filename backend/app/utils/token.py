from sqlalchemy.orm import Session

from app.models import ExpiredToken


def has_token_expired(db: Session, jwt_id: str) -> bool:
    return db.query(ExpiredToken).filter(ExpiredToken.jwt_id == jwt_id).first()

def add_expired_token(db: Session, jwt_id: str, user_id: int):
    db_token = ExpiredToken(jwt_id=jwt_id, user_id=user_id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)

    return db_token