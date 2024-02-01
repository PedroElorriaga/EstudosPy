from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


# ABRE A CONEXÃO, FAZ O USO E FECHA
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
