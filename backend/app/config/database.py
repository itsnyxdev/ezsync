from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import create_engine, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column

from .config import settings

mariadb_engine = create_engine(settings.MARIADB_URI, connect_args={
    "plugin_dir": settings.PLUGIN_DIR
})
mariadb_session_local = sessionmaker(autocommit=settings.MARIADB_AUTOCOMMIT, autoflush=settings.MARIADB_AUTOFLUSH, bind=mariadb_engine)
MariaDBBase = declarative_base()

def create_all_tables():
    from app.models import User, ExpiredToken
    MariaDBBase.metadata.create_all(bind=mariadb_engine)



class DatabaseManager:
    client: AsyncIOMotorClient = None # type: ignore
    database = None

database_manager = DatabaseManager()


async def mongodb_connect():
    database_manager.client = AsyncIOMotorClient(settings.MONGODB_URI)
    database_manager.database = database_manager.client[settings.MONGODB_DATABASE] # type: ignore

async def mongodb_disconnect():
    if database_manager.client:
        database_manager.client.close()

def get_mongodb():
    return database_manager.database




class TimestampMixin:
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

