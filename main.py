from fastapi import FastAPI
from models.user import User


app = FastAPI()

user_list = [
    User(id=1, name="juan", email="juan@gmail.com", password="12345678"),
    User(id=2, name="jorge", email="jorge@gmail.com", password="12345678"),
    User(id=3, name="jose", email="jose@gmail.com", password="12345678"),
]


@app.get("/users")
async def get_users():
    return user_list


def search_users(id):
    """Funcion que filtrara los datos y devolvera el usuario encontrado, si es que lo hay"""
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No existe el usuario"}


# get con path
@app.get("/user/{id}")
async def get_one_user(id: int):
    return search_users(id)


# get con query
@app.get("/userquery/")
async def get_one_user(id: int):
    return search_users(id)
