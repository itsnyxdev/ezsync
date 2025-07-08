from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from .config import settings

mariadb_engine = create_engine(settings.MARIADB_URI)
mariadb_session_local = sessionmaker(autocommit=settings.MARIADB_AUTOCOMMIT, autoflush=settings.MARIADB_AUTOFLUSH, bind=mariadb_engine)
MariaDBBase = declarative_base()
MariaDBBase.metadata.create_all(mariadb_engine)

class DatabaseManager:
    client: AsyncIOMotorClient = None
    database = None

database_manager = DatabaseManager()


async def mongodb_connect():
    database_manager.client = AsyncIOMotorClient(settings.MONGODB_URI)
    database_manager.database = database_manager.client[settings.MONGODB_DATABASE]

async def mongodb_disconnect():
    if database_manager.client:
        database_manager.client.close()

def get_mongodb():
    return database_manager.database

def get_mariadb() -> Session:
    db = mariadb_session_local()
    try:
        yield db
    finally:
        db.close()