from fastapi import FastAPI, Response, Request

from api import routers


app = FastAPI(
    title="Minha loja de veículos",
    description="Autor: Vanniery Fernandes",
    version="0.1"
)

app.include_router(routers.api_router)



