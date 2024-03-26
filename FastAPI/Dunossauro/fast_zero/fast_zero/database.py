from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.settings import Configuracoes

engine = create_engine(Configuracoes().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
