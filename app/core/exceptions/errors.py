from alembic.op import f


class AppError(Exception):
    """Base class for application-specific exceptions."""

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class NotFoundError(AppError):
    """Exception raised when a requested resource is not found."""

    def __init__(self, resource:str, key: str)-> None:
        super().__init__(f"{resource} with {key} not found.", status_code=404)


class ConflictError(AppError):
    """Exception raised when a conflict occurs, such as a duplicate entry."""

    def __init__(self, resource: str, key: str) -> None:
        super().__init__(f"{resource} with {key} already exists.", status_code=409)