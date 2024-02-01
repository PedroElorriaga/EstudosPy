from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings


engine: AsyncEngine = create_async_engine(
    settings.DB_URL)  # CRIA A CONEXÃO COM O BANCO DE DADOS

Session: AsyncSession = sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    class_=False,
    bind=engine
)
