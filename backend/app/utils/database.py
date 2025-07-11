from app.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

async def init_mariadb():
    engine = create_async_engine(settings.mariadb_uri, echo=False)
    session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    return session

async def close_mariadb(engine: AsyncEngine):
    await engine.dispose()
