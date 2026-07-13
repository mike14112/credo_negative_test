import allure
import pytest
from faker import Faker

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.env import Env

faker = Faker()

config = ConfigReader(env=Env.DEV.value)


@allure.feature('Authorization for login')
@allure.story("Login button state with empty fields")
@pytest.mark.parametrize(
    "language, user_name, password",
    [("georgian", faker.user_name(), faker.password(length=10, special_chars=True, digits=True)),
     ("მეგრული", faker.user_name(), faker.password(length=10, special_chars=True, digits=True)),
     ("სვანური", faker.user_name(), faker.password(length=10, special_chars=True, digits=True))])
def test_login_button_state(browser, language, user_name, password):
    login_page = LoginPage(browser)

    with allure.step("Open login page"):
        browser.driver.get(config.get("login_url"))
    with allure.step("Verify login button is disabled"):
        assert not login_page.is_login_button_enabled()

    with allure.step("Open language selector"):
        login_page.language_selector.click_btn_open_popup()

    with allure.step(f"Select {language} language"):
        if language == "georgian":
            login_page.language_selector.click_btn_georgian_lang()
        elif language == "megrelian":
            login_page.language_selector.click_btn_english_lang()
        elif language == "svanuri":
            login_page.language_selector.click_btn_russian_lang()

    with allure.step("Verify login button is disabled with empty fields"):
        assert not login_page.is_login_button_enabled()

    with allure.step(f"Fill input username: {user_name}"):
        login_page.fill_login_form(user_name)

    with allure.step("Clear input user field"):
        login_page.clear_input_login()

    with allure.step("Verify login button is disabled with empty input login fields"):
        assert not login_page.is_login_button_enabled()

    with allure.step("Fill input password"):
        login_page.fill_password_form(password)

    with allure.step("Clear input password field"):
        login_page.clear_input_password()

    with allure.step("Verify login button is disabled with empty input password fields"):
        assert not login_page.is_login_button_enabled()
