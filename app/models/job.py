from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(2000))
    salary: Mapped[float] = mapped_column(Float)
    company_id: Mapped[int] = mapped_column()

    applications = relationship("Application", back_populates="job", cascade="all, delete-orphan")
