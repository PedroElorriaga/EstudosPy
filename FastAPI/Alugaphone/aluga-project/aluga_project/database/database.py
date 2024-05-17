from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from aluga_project.setting.settings import Configs

engine = create_engine(Configs().DATABASE_URL)


def create_session():
    with Session(engine) as session:
        yield session
