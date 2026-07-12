from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader
from utils.env import Env

config = ConfigReader(env=Env.DEV.value)
options = Options()


class Browser:

    def __init__(self):
        options.add_argument(config.get("screen_size"))
        options.add_argument(config.get("no_sandbox"))
        self.driver = webdriver.Chrome(options=options)

    def get_driver(self):
        return self.driver

    def reload(self):
        self.driver.refresh()

    def quit(self):
        self.driver.quit()
