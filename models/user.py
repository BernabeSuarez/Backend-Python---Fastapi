from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    email: str
    isDisabled: bool


class UserDb(User):
    password: str
