import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from aluga_project.app import app
from aluga_project.database.database import create_session
from aluga_project.models.models import Base, PhoneStock


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
    phone_test = UserFactory()

    session.add(phone_test)
    session.commit()
    session.refresh(phone_test)

    return phone_test


class UserFactory(factory.Factory):
    class Meta:
        model = PhoneStock

    phone_model = 'S22'
    brand = 'Samsung'
    chip = False
    color = 'Black'
    price = 2.500
