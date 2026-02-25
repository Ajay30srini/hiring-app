from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.crud.security import hash_password

def create_user(db: Session, data: UserCreate) -> User:
    user = User(
        name=data.name,
        email=data.email,
        role=data.role,
        hashed_password=hash_password(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))

def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)
