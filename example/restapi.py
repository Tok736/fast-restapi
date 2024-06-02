from fast_restapi import BaseRestAPI

from models import User
from schemas import UserReadSchema, UserCreateSchema, UserUpdateSchema
from database import get_async_session


class UserRestAPI(BaseRestAPI, model=User):
    """ User class with basic endpoint """

    create_schema = UserCreateSchema
    read_schema = UserReadSchema
    update_schema = UserUpdateSchema


user_restapi = UserRestAPI(get_async_session)
