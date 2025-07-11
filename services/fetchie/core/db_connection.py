from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from loguru import logger
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure, OperationFailure, ConfigurationError


class DBConnection:
    _instance = None
    _connection = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.connect()
            logger.info("Database connection instance created.")
        else:
            logger.debug("Database connection instance already initialized.")

    def connect(self):
        if self._connection is None:
            logger.info(f"Attempting to connect to MongoDB at {DB_HOST}:{DB_PORT}...")
            try:
                db_uri = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"
                connection = MongoClient(db_uri)
                connection.ezsync.command("ping")
                self._connection = connection[DB_NAME]
                logger.info("Connection was successful!")
            except Exception as e:
                logger.error(f"Connection failed: {e}")


    def get_db(self):
        if self._connection is None:
            self.connect()
        return self._connection