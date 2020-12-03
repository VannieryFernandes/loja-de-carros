from fastapi import APIRouter

router = APIRouter()

@router.post("/entrar")
def entrar():
    return "Autenticando"