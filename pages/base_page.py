class BasePage:
    LOC_UNIQUE_ELEM = None

    def __init__(self, browser):
        self.browser = browser
        self.page_name = None
        self.unique_elem = None

    def wait_for_element(self):
        return self.unique_elem.wait_for_presence()