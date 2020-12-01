from fastapi import APIRouter


from api.veiculos.v1 import veiculosRecursos
from api.autenticacao.v1 import autenticacaoRecursos




api_router = APIRouter()
api_router.include_router(autenticacaoRecursos.router, tags=["autenticacao"])
api_router.include_router(veiculosRecursos.router, prefix="/veiculos", tags=["veiculos"])
