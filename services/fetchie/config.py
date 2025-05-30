import os
from dotenv import load_dotenv

load_dotenv()

DRIVER_PATH = os.getenv("DRIVER_PATH")
DRIVER_PROFILE_PATH = os.getenv("DRIVER_PROFILE_PATH")

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")
