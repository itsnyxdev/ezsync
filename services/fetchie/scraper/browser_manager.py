import os
import random
import time
from urllib.parse import urlencode

from selenium.webdriver.common.actions.action_builder import ActionBuilder

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
        width, height = (random.randint(800, 1920), random.randint(600, 1080))

        service = Service(config.DRIVER_PATH)
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={os.path.abspath(config.DRIVER_PROFILE_PATH)}")
        options.add_argument(f"window-size={width},{height}")


        self._driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        if not self._driver:
            logger.error("WebDriver hasn't been initialized.")
        return self._driver

    def quit_driver(self):
        if self._driver:
            self._driver.quit()
            logger.info("WebDriver quit successfully.")
            return True
        else:
            logger.error("WebDriver is not initialized, cannot quit.")
            return False

    def random_wait(self, min=1, max=5):
        time.sleep(random.uniform(min, max))

    @staticmethod
    def random_mouse_position(self):
        width, height = self.get_viewports()
        x = random.random() * width
        y = random.random() * height

        action = ActionBuilder(self._driver)
        action.pointer_action.move_by(x, y)
        action.perform()

    def scroll_down(self):
        self._driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
        self.random_wait(1,3)


    def get_viewports(self):
        window = self._driver.get_window_size()
        height = window['height']
        width = window['width']

        return width, height

    @staticmethod
    def create_url(endpoint, params=None):
        if not params:
            return endpoint

        query_str = urlencode(params)
        final_url = f"{endpoint}?{query_str}"

        return final_url