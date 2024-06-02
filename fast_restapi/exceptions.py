from pydantic import BaseModel
from fastapi import HTTPException, status

from .enums import SchemaType

class BaseHTTPException(HTTPException):
    """ Base exception for HTTP error codes """

    def __init__(
        self, 
        status_code: int, 
        detail:      str,
        description: str
    ) -> None:
        self.description = description
        super().__init__(status_code, detail)


class NotFoundException(BaseHTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_404_NOT_FOUND, 
        detail:      str = "Not found",
        description: str = "Error that appear when resource is not found"
    ) -> None:
        super().__init__(status_code, detail, description)


class ValidationErrorException(BaseHTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY, 
        detail:      str = "Validation error",
        description: str = "Error when sended data is not valid"
    ) -> None:
        super().__init__(status_code, detail, description)


class ConflictException(BaseHTTPException):
    def __init__(
        self, 
        status_code: int = status.HTTP_409_CONFLICT, 
        detail:      str = "Conflict while adding/updating resource",
        description: str = "Error when trying to modify/add a resource that cannot be created or cannot be updated"
    ) -> None:
        super().__init__(status_code, detail, description)


class SchemaNotSpecified(Exception):
    """ Custom exception, when schema for creating endpoint is not specified """
    
    def __init__(self, schema: SchemaType, endpoint: str) -> None:
        super().__init__(
            f"Schema '{schema.value}' is needed to be specified to create endpoint '{endpoint}'."
        )

