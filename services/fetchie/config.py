import os
from dotenv import load_dotenv

load_dotenv()

DRIVER_PATH = os.getenv("DRIVER_PATH")
DRIVER_PROFILE_PATH = os.getenv("DRIVER_PROFILE_PATH")

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")

ENDPOINT_FEED = os.getenv("ENDPOINT_FEED")
ENDPOINT_LOGIN = os.getenv("ENDPOINT_LOGIN")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
