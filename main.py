from fastapi import FastAPI
from routes import user
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(user.router)
# servir contenido estatico
app.mount("/static", StaticFiles(directory="static"), name="static")
