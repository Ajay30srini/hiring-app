from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.job import JobCreate, JobUpdate, JobOut
from app.crud.job import create_job, get_job, update_job, delete_job, list_jobs

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("", response_model=JobOut, status_code=201)
def create(payload: JobCreate, db: Session = Depends(get_db)):
    return create_job(db, payload)

@router.get("", response_model=list[JobOut])
def list_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_jobs(db, skip=skip, limit=limit)

@router.get("/{job_id}", response_model=JobOut)
def get_one(job_id: int, db: Session = Depends(get_db)):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")
    return job

@router.put("/{job_id}", response_model=JobOut)
def update(job_id: int, payload: JobUpdate, db: Session = Depends(get_db)):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")
    return update_job(db, job, payload)

@router.delete("/{job_id}", status_code=204)
def remove(job_id: int, db: Session = Depends(get_db)):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")
    delete_job(db, job)
    return None
