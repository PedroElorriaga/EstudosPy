import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from aluga_project.app import app
from aluga_project.database.database import create_session
from aluga_project.models.models import Base, PhoneStock, UserModels
from aluga_project.security.security import make_password_hash


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[create_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def phone_factory(session):
    phone_test = PhoneFactory()

    session.add(phone_test)
    session.commit()
    session.refresh(phone_test)

    return phone_test


@pytest.fixture
def user_factory(session):
    user_test = UserFactory()

    session.add(user_test)
    session.commit()
    session.refresh(user_test)

    user_test.clean_password = 'test'  # Monkey patch

    return user_test


@pytest.fixture
def user_second_factory(session):
    user_test = UserFactory()

    session.add(user_test)
    session.commit()
    session.refresh(user_test)

    user_test.clean_password = 'test'  # Monkey patch

    return user_test


@pytest.fixture
def token(client, user_factory):
    response = client.post(
        '/token',
        data={
            'username': user_factory.email,
            'password': user_factory.clean_password,
        },
    )

    return response.json()['access_token']


class PhoneFactory(factory.Factory):
    class Meta:
        model = PhoneStock

    phone_model = 'S22'
    brand = 'Samsung'
    chip = False
    color = 'Black'
    price = 2.500


class UserFactory(factory.Factory):
    class Meta:
        model = UserModels

    first_name = 'Jhon'
    middle_name = 'Doe'
    cpf = 61989645828
    active_account = True
    active_rent = False
    email = 'jhon@test.com'
    password = make_password_hash('test')
