from fastapi import APIRouter

router = APIRouter()


@router.get("/lista-de-veiculos")
async def lista_carros():
    return []