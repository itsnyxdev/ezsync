from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

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
    

settings = Settings()