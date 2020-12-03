from fastapi import APIRouter

router = APIRouter()


@router.get("/lista-de-veiculos")
def lista_carros():
    return []