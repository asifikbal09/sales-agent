from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.APP_NAME)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/health", tags=["Health"] )
def health():
    return {"status": "ok","app": settings.APP_NAME}

