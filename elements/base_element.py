from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)


class BaseElement:
    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator
        self.wait = config.get('wait')
        self.pull = config.get('fast_pull_frequency')

        if isinstance(locator, str):
            if '/' in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

    def wait_for_visibility(self):
        try:
            return WebDriverWait(self.browser.driver, self.wait, ).until(
                EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            raise

    def wait_for_presence(self, pull=False):
        if pull:
            pull = self.pull
        try:
            return WebDriverWait(self.browser.driver, self.wait, poll_frequency=pull).until(
                EC.presence_of_element_located(self.locator))
        except TimeoutException:
            raise

    def get_text(self):
        element = self.wait_for_presence()
        return element.text

    def wait_until_text_contains(self, expected_text):
        WebDriverWait(self.browser.driver, self.wait).until(
            lambda driver: expected_text.strip() in self.get_text().strip()
        )
        return self.get_text()

    def click(self):
        element = self.wait_for_visibility()
        element.click()

    def send_keys(self, keys):
        element = self.wait_for_presence()
        element.clear()
        return element.send_keys(keys)

    def clear_field(self):
        element = self.wait_for_presence()
        element.clear()

    def btn_is_enabled(self):
        element = self.wait_for_presence()
        return element.is_enabled()
