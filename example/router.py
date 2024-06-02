from fastapi import APIRouter, Depends
from sqlalchemy import select, insert

from schemas import UserCreateSchema, UserReadSchema, UserUpdateSchema 
from database import get_async_session, AsyncSession
from models import User

from restapi import user_restapi

router = user_restapi.get_router()


# router = APIRouter()

# async def get_user_by_id(**kwargs):

#     id = kwargs["id"]
#     session = kwargs["session"]

#     statement = select(User).where(User.id == id)
#     return await session.scalar(statement)

# from inspect import Signature, Parameter, _ParameterKind

# get_user_by_id.__signature__ = Signature(
#     parameters=[
#         Parameter("id", _ParameterKind.POSITIONAL_OR_KEYWORD, annotation=int),
#         Parameter("session", _ParameterKind.POSITIONAL_OR_KEYWORD, default=Depends(get_async_session), annotation=AsyncSession),
#     ],
#     return_annotation=UserReadSchema
# )

# from inspect import signature

# print(f"!!!! {signature(get_user_by_id)}")


# router.get("/users/{id}")(get_user_by_id)



# async def get_users(**kwargs):
#     session = kwargs["session"]

#     statement = select(User)
#     return await session.scalars(statement)

# from inspect import Signature, Parameter, _ParameterKind

# p = Parameter(
#     'session', 
#     kind=_ParameterKind.KEYWORD_ONLY, 
#     default=Depends(get_async_session), 
#     annotation=AsyncSession
# )
# s = Signature(parameters=[p], return_annotation=list[UserReadSchema])

# get_users.__signature__ = s

# router.get("/users")(get_users)


# async def create_user(**kwargs):
#     session = kwargs["session"]
#     user = kwargs["user"]
    
#     statement = insert(
#         User
#     ).values(
#         **user.model_dump()
#     ).returning(
#         User
#     )

#     result = await session.scalar(statement)
#     await session.commit()

#     return result

# create_user.__signature__ = Signature(
#     parameters=[
#         Parameter("user", _ParameterKind.KEYWORD_ONLY, annotation=UserCreateSchema),
#         Parameter("session", _ParameterKind.KEYWORD_ONLY, default=Depends(get_async_session), annotation=AsyncSession)
#     ],
#     return_annotation=UserReadSchema
# )

# router.post("/users")(create_user)


# user: UserCreateSchema,
# session: AsyncSession = Depends(get_async_session),

