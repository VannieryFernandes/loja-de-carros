import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from starlette.requests import Request

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
#
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

def get_db(request: Request):
    print(request)
    return request.state.db