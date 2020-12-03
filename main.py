from fastapi import FastAPI, Response, Request
from app.v1 import routers
from app.core.db import  engine,SessionLocal

app = FastAPI(
    title="Minha loja de veículos",
    description="Autor: Vanniery Fernandes",
    version="0.1"
)
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routers.api_router)
