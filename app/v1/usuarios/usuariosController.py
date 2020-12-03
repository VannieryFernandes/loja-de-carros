from typing import Optional

from sqlalchemy.orm import Session

from app.v1.usuarios.usuariosModels import Usuario
from app.v1.usuarios.usuariosSchema import UserCreate, UserUpdate



class UserController(Usuario):
    def get_by_email( db_session: Session, email: str) -> Optional[Usuario]:
        return db_session.query(Usuario).filter(Usuario.email == email).first()

    def create(db_session: Session, obj_in: UserCreate) -> Usuario:
        db_obj = Usuario(
            email=obj_in.email,
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
            password=obj_in.password
        )
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj