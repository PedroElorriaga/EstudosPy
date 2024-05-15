from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from aluga_project.setting.settings import configs

engine = create_engine(configs.DATABASE_URL)


def create_session():
    with Session(engine) as session:
        yield session
