from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import Settings, get_settings
from app.core.exceptions.handlers import register_exception_handlers
from app.db.session import SessionDep, get_session
from app.api.v1.router import api_router




app = FastAPI(title=get_settings().APP_NAME, debug=get_settings().DEBUG)
register_exception_handlers(app)
app.include_router(router=api_router)

@app.get("/health")
async def health(settings: Settings = Depends(get_settings))-> dict[str, str]:
    return {
        "status": "ok",
        "app_name": settings.APP_NAME
    }


@app.get("/health/db")
async def health_db(session: SessionDep) -> dict[str, str]:
    result = await session.execute(
        text(text="SELECT version();")
    )
    version = result.scalar_one()

    ext = await session.execute(
        text(text="SELECT extname FROM pg_extension WHERE extname='vector';")
    )
    has_vector = ext.scalar_one_or_none() is not None

    return {
        "database": "connected",
        "version": version,
        "has_vector": "yes" if has_vector else "no"
    }