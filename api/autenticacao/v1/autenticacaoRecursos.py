from fastapi import APIRouter


router = APIRouter()


@router.post("/entrar")
async def entrar():
    return "Autenticando"