from fastapi_csrf_protect import CsrfProtect
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    algorithm: str
    secret_key: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int

    mariadb_name: str
    mariadb_user: str
    mariadb_password: str
    mariadb_host: str
    mariadb_port: str
    mariadb_uri: str

    mongodb_name: str
    mongodb_user: str
    mongodb_password: str
    mongodb_host: str
    mongodb_port: str
    mongodb_uri: str

    test_mariadb_name: str
    test_mariadb_uri: str

class CsrfSettings(BaseSettings):
    secret_key: str = "secret_key"


settings = Settings()

