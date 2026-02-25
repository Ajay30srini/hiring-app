from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    role: Mapped[str] = mapped_column(String(50))  # 'hr' or 'candidate'
    hashed_password: Mapped[str] = mapped_column(String(255))

    applications = relationship("Application", back_populates="user", cascade="all, delete-orphan")
