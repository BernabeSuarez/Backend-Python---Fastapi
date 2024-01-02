from fastapi import APIRouter, Depends
from models.user import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    pass
