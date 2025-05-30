import os
import config

from loguru import logger

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BrowserManager:
    _instance = None
    _driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BrowserManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            logger.info("BrowserManager initialized.")
        else:
            logger.info("BrowserManager instance already exists.")

    def init_driver(self):
        service = Service(config.DRIVER_PATH)
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={os.path.abspath(config.DRIVER_PROFILE_PATH)}")

        self._driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        if not self._driver:
            logger.error("WebDriver hasn't been initialized.")
        return self._driver

    def quit_driver(self):
        if self._driver:
            self._driver.quit()
            logger.info("WebDriver quit successfully.")
        else:
            logger.error("WebDriver is not initialized, cannot quit.")
