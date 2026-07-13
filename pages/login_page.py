from component.language_selector import LanguageSelector
from elements.web_element import WebElement
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOQ_LANG_TEXT = 'forgotPass'
    LOQ_LOGIN_INPUT = 'userName'
    LOQ_PASSWORD_INPUT = 'newPass'
    LOQ_BTN_SIGN_IN = 'submitAuth'
    LOQ_ERROR_TXT = 'growlText'

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.page_name = 'login page'
        self.lang_text = WebElement(self.browser, self.LOQ_LANG_TEXT)
        self.login_input = WebElement(self.browser, self.LOQ_LOGIN_INPUT)
        self.password_input = WebElement(self.browser, self.LOQ_PASSWORD_INPUT)
        self.btn_sign_in = WebElement(self.browser, self.LOQ_BTN_SIGN_IN)
        self.error_text = WebElement(self.browser, self.LOQ_ERROR_TXT)

        self.language_selector = LanguageSelector(self.browser)

    def get_changing_text(self, text):
        return self.lang_text.wait_until_text_contains(text)

    def get_text(self):
        return self.lang_text.get_text()

    def fill_login_form(self, text):
        self.login_input.send_keys(text)

    def fill_password_form(self, text):
        self.password_input.send_keys(text)

    def clear_input_login(self):
        self.login_input.clear_field()
    def clear_input_password(self):
        self.password_input.clear_field()

    def click_btn_login(self):
        self.btn_sign_in.click()

    def is_login_button_enabled(self):
        self.btn_sign_in.btn_is_enabled()

    def get_error(self):
        return self.error_text.get_text()
