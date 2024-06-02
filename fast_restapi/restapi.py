from typing import Callable, AsyncGenerator

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta

from .repository import BaseRepository
from .function_fabrics import FunctionFabric


class BaseRestAPI:
    """ Main class to make RestAPI endpoints """

    model: DeclarativeMeta

    create_schema: BaseModel | None = None
    read_schema:   BaseModel | None = None
    update_schema: BaseModel | None = None

    model_name:        str | None = None 
    model_name_plural: str | None = None
    

    def get_repository(self) -> BaseRepository:
        return self.repository    

    def create_get_by_id(self) -> None:
        """ Creates 'get_by_id' endpoint """

        self.router.get(
            "/" + self.model_name_plural + "/{id}"
        )(
            self.function_fabric.create_get_by_id()
        )

    def _create_endpoints(self, router: APIRouter):
        """ Create all endpoints """

        self.create_get_by_id()

        
    def __init__(self, get_async_session: Callable[[], AsyncGenerator[AsyncSession, None]]) -> None:
        self.get_async_session = get_async_session
        
        if self.model_name is None:
            self.model_name = self.model.__tablename__
        if self.model_name_plural is None:
            self.model_name_plural = self.model_name + "s"

        self.repository = BaseRepository[
            self.model, 
            self.create_schema,
            self.read_schema, 
            self.update_schema,
        ](
            self.model,
            self.model_name,
            self.model_name_plural,
        )

        self.router = APIRouter()
        
        self.function_fabric = FunctionFabric(
            self.model, 
            self.repository,
            self.create_schema,
            self.read_schema,
            self.update_schema,
            self.get_async_session,
            self.model_name,
            self.model_name_plural,
        )

        self._create_endpoints(self.router)

    def __init_subclass__(cls, model: DeclarativeMeta) -> None:
        cls.model = model

    def get_router(self) -> APIRouter:
        """ Returns constructed router """

        return self.router
        
