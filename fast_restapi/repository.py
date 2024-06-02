from typing import Generic, TypeVar

from sqlalchemy import select, update, insert, delete
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession


from .exceptions import NotFoundException


model_type = TypeVar("model_type")
create_schema = TypeVar("create_schema")
read_schema = TypeVar("read_schema")
update_schema = TypeVar("update_schema")

class BaseRepository(Generic[model_type, create_schema, read_schema, update_schema]):
    """ Base class to interact with database """

    def __init__(
        self, 
        model: DeclarativeBase,
        model_name: str,
        model_name_plural: str,
    ):
        self.model = model
        self.model_name = model_name
        self.model_name_plural = model_name_plural

    async def get_by_id(self, id: int, session: AsyncSession) -> model_type:
        """ Return a one model object by id """

        statement = select(self.model).where(self.model.id == id)
        result = await session.scalar(statement)

        if not result:
            raise NotFoundException(
                detail=f"Resource '{self.model_name}' with id = '{id}' is not found"
            )
        
        return result
            


