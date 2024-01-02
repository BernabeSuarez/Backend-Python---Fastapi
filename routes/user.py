from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.user import User
from db.client import client
from schemas.user_schema import users_schema, user_schema

router = APIRouter()

db = client.get_database("fastapi")


@router.get("/users")
async def get_users():
    data = db.users.find()
    return users_schema(data)


# get con path
@router.get("/user/{id}")
async def get_one_user(id: str):
    data = db.users.find_one({"_id": id})
    return data


# post
@router.post("/create-user")
async def create_user(user: User):
    new_user = jsonable_encoder(user)
    usuario = db.users.insert_one(new_user)
    final_user = db.users.find_one({"_id": usuario.inserted_id})
    return final_user
