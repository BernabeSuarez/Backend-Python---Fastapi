from fastapi import APIRouter
from models.user import User

router = APIRouter()

user_list = [
    User(id=1, name="juan", email="juan@gmail.com", password="12345678"),
    User(id=2, name="jorge", email="jorge@gmail.com", password="12345678"),
    User(id=3, name="jose", email="jose@gmail.com", password="12345678"),
]


@router.get("/users")
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
@router.get("/user/{id}")
async def get_one_user(id: int):
    return search_users(id)


# get con query
@router.get("/userquery/")
async def get_one_user(id: int):
    return search_users(id)


# post


@router.post("/create-user")
async def create_user(user: User):
    # Agregar un nuevo registro a la lista de usuarios
    if type(search_users(user.id)) == User:  # comprueba si el id ya existe
        return {"message": "El usuario ya existe"}
    else:
        user_list.append(user)
