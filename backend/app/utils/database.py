from typing import AsyncGenerator

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.models.document import Category, Job

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

async def init_mongodb():
    client = AsyncIOMotorClient(settings.mongodb_uri)
    await init_beanie(database=client[settings.mongodb_name], document_models=[Category, Job])
