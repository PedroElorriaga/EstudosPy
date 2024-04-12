import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import Base, Usuario
from fast_zero.security import criar_hash_de_senha


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
    senha = 'testsoft'
    usuario = UserFactory(senha=criar_hash_de_senha(senha))

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    # hook no modelo que processa os dados antes de salvá-los no banco de dados
    usuario.clean_password = 'testsoft'

    return usuario


@pytest.fixture
def outro_usuario(session):
    senha = 'testsoft'
    usuario = UserFactory(senha=criar_hash_de_senha(senha))

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    # hook no modelo que processa os dados antes de salvá-los no banco de dados
    usuario.clean_password = 'testsoft'

    return usuario


@pytest.fixture
def token(client, usuario):
    response = client.post(
        '/auth/token',
        data={'username': usuario.email, 'password': usuario.clean_password},
    )

    return response.json()['access_token']


class UserFactory(factory.Factory):
    class Meta:
        model = Usuario

    id = factory.Sequence(lambda n: n)
    username = factory.LazyAttribute(lambda obj: f'test{obj.id}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    senha = factory.LazyAttribute(lambda obj: f'{obj.username}123')
