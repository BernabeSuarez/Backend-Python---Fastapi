from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    # firstName: str
    # lastName: str
    # isVerified: bool = Field(default=False)
