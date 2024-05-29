from pydantic import BaseModel


class UserReadSchema(BaseModel):
    id:     int
    email:  str



