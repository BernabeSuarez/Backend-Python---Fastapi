from fastapi import FastAPI
from routes import user, basic_auth_user
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(user.router)
app.include_router(basic_auth_user.router)
# servir contenido estatico
app.mount("/static", StaticFiles(directory="static"), name="static")
