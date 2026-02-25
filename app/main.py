from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.user_routes import router as user_router
from app.api.v1.job_routes import router as job_router
from app.api.v1.application_routes import router as application_router

app = FastAPI(title=settings.APP_TITLE)

app.include_router(user_router)
app.include_router(job_router)
app.include_router(application_router)

@app.get("/")
def health():
    return {"status": "ok", "app": settings.APP_TITLE}
