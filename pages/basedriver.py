import os
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from utils.utilities import Utilities


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        custom_logger = Utilities(self.driver)
        self.log = custom_logger.get_logger()


    def capture_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"screenshots/{name}_{timestamp}.png"
        os.makedirs(os.path.dirname(screenshot_name), exist_ok=True)
        self.driver.save_screenshot(screenshot_name)
        self.log.info(f"Screenshot captured: {screenshot_name}")
