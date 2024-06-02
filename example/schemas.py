from pydantic import BaseModel


class UserReadSchema(BaseModel):
    id:       int
    email:    str

class UserCreateSchema(BaseModel):
    email:    str
    password: str

class UserUpdateSchema(BaseModel):
    email:    str | None
    password: str | None