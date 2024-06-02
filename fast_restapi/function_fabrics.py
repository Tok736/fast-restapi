from typing import Callable, Any, Type, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel

from .repository import BaseRepository
from .enums import SchemaType
from .exceptions import SchemaNotSpecified


class FunctionFabric:
    """ Class for creating api functions """

    def __init__(
        self, 
        model: DeclarativeBase,
        repository: BaseRepository,
        create_schema: Type[BaseModel],
        read_schema:   Type[BaseModel],
        update_schema: Type[BaseModel],
        get_async_session: Callable[[], AsyncGenerator[AsyncSession, None]],
        model_name: str,
        model_name_plural: str,
    ) -> None:
        self.model = model
        self.repository = repository
        self.create_schema = create_schema
        self.read_schema = read_schema
        self.update_schema = update_schema
        self.get_async_session = get_async_session
        self.model_name = model_name
        self.model_name_plural = model_name_plural

    def create_get_by_id(self) -> Callable[..., Any]:
        """ Returns get_by_id function """

        endpoint_name = f"get_{self.model_name}_by_id"

        if self.read_schema is None:
            raise SchemaNotSpecified(SchemaType.read_schema, endpoint_name)

        async def get_by_id(id: int, session: AsyncSession = Depends(self.get_async_session)) -> self.read_schema:
            return await self.repository.get_by_id(id, session)

        get_by_id.__name__ = endpoint_name

        return get_by_id
