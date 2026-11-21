

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions.errors import ConflictError, NotFoundError


def register_exception_handlers(app: FastAPI)-> None:
    @app.exception_handler(exc_class_or_status_code=404)
    async def not_found(_:Request, exc: NotFoundError)->JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message},
        )
    @app.exception_handler(exc_class_or_status_code=ConflictError)
    async def conflict(_:Request, exc: ConflictError)->JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message},
        )