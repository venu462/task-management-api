from sqlalchemy.orm import Session
from app.models.user_model import Users
from app.core.security import hash_password
from app.schemas.user_schema import UserCreate


def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed = hash_password(user.password)
    db_user = Users(
        email=user.email,
        hash_password=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

