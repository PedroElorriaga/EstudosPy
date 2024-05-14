from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine()


def create_session():
    with Session(engine) as session:
        yield session
