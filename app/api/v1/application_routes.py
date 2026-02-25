from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.application import ApplicationCreate, ApplicationOut
from app.crud.application import create_application
from app.crud.user import get_user
from app.crud.job import get_job

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("", response_model=ApplicationOut, status_code=201)
def apply(payload: ApplicationCreate, db: Session = Depends(get_db)):
    if not get_user(db, payload.user_id):
        raise HTTPException(status_code=404, detail="User not found.")
    if not get_job(db, payload.job_id):
        raise HTTPException(status_code=404, detail="Job not found.")
    return create_application(db, payload)
