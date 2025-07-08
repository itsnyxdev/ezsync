import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    SECRET_KEY_ALGORITHM: str = os.getenv("SECRET_KEY_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN"))

    MARIADB_USER: str = os.getenv("MARIADB_USER")
    MARIADB_PASSWORD: str = os.getenv("MARIADB_PASSWORD")
    MARIADB_HOST: str = os.getenv("MARIADB_HOST")
    MARIADB_PORT: str = os.getenv("MARIADB_PORT")
    MARIADB_DATABASE: str = os.getenv("MARIADB_DATABASE")
    MARIADB_URI: str = f"mariadb+mariadbconnector://{MARIADB_USER}:{MARIADB_PASSWORD}@{MARIADB_HOST}:{MARIADB_PORT}/{MARIADB_DATABASE}"

    MARIADB_AUTOCOMMIT: bool = False
    MARIADB_AUTOFLUSH: bool = False

    MONGODB_USER: str = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD: str = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST: str = os.getenv("MONGODB_HOST")
    MONGODB_PORT: str = os.getenv("MONGODB_PORT")
    MONGODB_DATABASE: str = os.getenv("MONGODB_DATABASE")
    MONGODB_URI: str = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/?authSource=admin"

settings = Settings()