from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate

def create_job(db: Session, data: JobCreate) -> Job:
    job = Job(**data.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def get_job(db: Session, job_id: int) -> Job | None:
    return db.get(Job, job_id)

def update_job(db: Session, job: Job, data: JobUpdate) -> Job:
    payload = data.model_dump(exclude_unset=True)
    for k, v in payload.items():
        setattr(job, k, v)
    db.commit()
    db.refresh(job)
    return job

def delete_job(db: Session, job: Job) -> None:
    db.delete(job)
    db.commit()

def list_jobs(db: Session, skip: int = 0, limit: int = 10) -> list[Job]:
    stmt = select(Job).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())
