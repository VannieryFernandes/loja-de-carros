from fastapi import APIRouter

router = APIRouter()

@router.get("/lista-de-clientes")
def lista_clientes():
    return {"Hello":"Clientes"}