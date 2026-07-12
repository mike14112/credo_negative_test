import allure
import pytest
from faker import Faker

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.env import Env

faker = Faker()

config = ConfigReader(env=Env.DEV.value)
EXCEPTED_ERROR_TEXT = 'მონაცემოლ სწორ დემეგ ლი'.lower().strip()
EXCEPTED_LANG = 'მონაცემოლე აღდგენა'.strip().lower()


@allure.feature('Authorization for login')
@allure.story("Login with invalid credentials in Svanuri language")
@pytest.mark.parametrize('user_name, password',
                         [(faker.password(length=1, special_chars=False, digits=False, upper_case=False,
                                          lower_case=True),
                           faker.password(length=1, special_chars=False, digits=False, upper_case=False,
                                          lower_case=True),),
                          (faker.user_name(),
                           faker.password(length=7, special_chars=True, digits=True, upper_case=False, )),
                          (faker.email(),
                           faker.password(length=250, special_chars=True, digits=True, upper_case=False)),
                          (faker.password(length=4, special_chars=True, digits=False, upper_case=False,
                                          lower_case=True),
                           faker.password(length=4, special_chars=True, digits=False, upper_case=False,
                                          lower_case=True))])
def test_negative_svanuri(browser, user_name, password):
    login_page = LoginPage(browser)
    with allure.step("Open login page"):
        browser.driver.get(config.get("login_url"))

    with allure.step("Open language selector"):
        login_page.language_selector.click_btn_open_popup()

    with allure.step("Select Svanuri language"):
        login_page.language_selector.click_btn_svanuri_lang()

    with allure.step("Verify that the page switched to Svanuri language"):
        actual_language_text = login_page.get_changing_text(EXCEPTED_LANG)
        assert EXCEPTED_LANG in actual_language_text, f'Excepted  message: {EXCEPTED_LANG} not in {actual_language_text}'

    with allure.step(f"Fill username: {user_name}"):
        login_page.fill_login_form(user_name)

    with allure.step("Fill password"):
        login_page.fill_password_form(password)

    with allure.step("Click Login button"):
        login_page.click_btn_login()

    with allure.step("Verify error message for invalid credentials"):
        actual_err_text = login_page.get_error()
        assert EXCEPTED_ERROR_TEXT in actual_err_text, (f'Excepted error message: {EXCEPTED_ERROR_TEXT}'
                                                        f' Not in {actual_err_text}')
