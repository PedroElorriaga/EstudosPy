import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import Base, Usuario


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # O TESTE É FEITO COM SQLITE EM MEMÓRIA
    engine = create_engine(
        'sqlite:///:memory:',
        # Threads e conexões
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def usuario(session):
    usuario = Usuario(
        username='teste', email='teste@email.com', senha='senha123'
    )
    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario
