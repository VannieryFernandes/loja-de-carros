from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Usuario(Base):
    __tablename__ = 'usuarios'    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)    
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    password = Column(String, index=True)
