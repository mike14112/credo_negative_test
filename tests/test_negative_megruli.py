import allure
import pytest
from faker import Faker

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from utils.env import Env

faker = Faker()

config = ConfigReader(env=Env.DEV.value)
EXCEPTED_ERROR_TEXT = 'მუნაჩემეფი ვა რე თინუ'.lower().strip()
EXCEPTED_ACTUAL_LANG = 'მუნაჩემუეფიშ ახალშო ენწყუალა'.strip().lower()


@allure.feature('Authorization for login Megruli language')
@allure.story("Login with invalid credentials in Megrelian language")
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
def test_negative_megruli(browser, user_name, password):
    login_page = LoginPage(browser)
    with allure.step("Open login page"):
        browser.driver.get(config.get("login_url"))

    with allure.step("Open language selector"):
        login_page.language_selector.click_btn_open_popup()

    with allure.step("Select Megruli language"):
        login_page.language_selector.click_btn_megruli_lang()

    with allure.step("Verify that the page switched to Megruli"):
        actual_language_text = login_page.get_changing_text(EXCEPTED_ACTUAL_LANG)
        assert EXCEPTED_ACTUAL_LANG in actual_language_text, (f'Excepted error message: {EXCEPTED_ACTUAL_LANG} '
                                                              f'Not in {actual_language_text}')

    with allure.step(f"Fill username: {user_name}"):
        login_page.fill_login_form(user_name)

    with allure.step("Fill password"):
        login_page.fill_password_form(password)

    with allure.step("Click Login button"):
        login_page.click_btn_login()

    with allure.step("Verify error message for invalid credentials"):
        actual_err_msg = login_page.get_error()
        assert EXCEPTED_ERROR_TEXT in actual_err_msg, (f'Excepted error message: {EXCEPTED_ERROR_TEXT}'
                                                      f' Not in {actual_err_msg}')
