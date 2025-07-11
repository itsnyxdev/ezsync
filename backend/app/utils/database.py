from typing import AsyncGenerator

from app.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from app.models import Base

engine = create_async_engine(settings.mariadb_uri, echo=True, future=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def init_mariadb():
    async with engine.begin() as connection:
        await  connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

async def close_mariadb(engine: AsyncEngine):
    await engine.dispose()
