from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models.application import Application
from app.schemas.application import ApplicationCreate

def create_application(db: Session, data: ApplicationCreate) -> Application:
    application = Application(user_id=data.user_id, job_id=data.job_id)
    try:
        db.add(application)
        db.commit()
        db.refresh(application)
        return application
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate application or invalid user/job.")
