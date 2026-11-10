from fastapi import FastAPI, Depends
from app.core.config import Settings, get_settings




app = FastAPI(title=get_settings().APP_NAME, debug=get_settings().DEBUG)

@app.get("/health")
async def health(settings: Settings = Depends(get_settings))-> dict[str, str]:
    return {
        "status": "ok",
        "app_name": settings.APP_NAME
    }