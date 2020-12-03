from fastapi import APIRouter, Body, Depends, HTTPException
from app.v1.usuarios.usuariosController import UserController
from app.v1.usuarios.usuariosSchema import User, UserCreate
from app.core.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/criar-usuario", response_model=User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate
    # current_user: DBUser = Depends(get_current_active_superuser),
):
    """
    Create new user.
    """
    user = UserController.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Usuário já cadastrado.",
        )
    user = UserController.create(db, obj_in=user_in)

    return user