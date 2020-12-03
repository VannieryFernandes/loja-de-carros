from fastapi import APIRouter
from app.v1.veiculos import veiculosRecursos
from app.v1.autenticacao import autenticacaoRecursos
from app.v1.usuarios import usuariosRecursos

api_router = APIRouter()
api_router.include_router(autenticacaoRecursos.router, tags=["autenticacao"])
api_router.include_router(veiculosRecursos.router, prefix="/veiculos", tags=["veiculos"])
api_router.include_router(usuariosRecursos.router, prefix="/usuarios", tags=["usuarios"])
