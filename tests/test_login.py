from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


VALID_EMAIL = "manuel11@gmail.com"
VALID_PASSWORD = "Manuel12345$"

INVALID_EMAIL = "manuelgmail.com"
INVALID_PASSWORD = "WrongPassword123$"

UNREGISTERED_EMAIL = "unknown_user_987654@gmail.com"


def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in(VALID_EMAIL, VALID_PASSWORD)

    assert login_page.get_account_link_text() is not None, \
        "Login was not successful"

    assert not login_page.is_login_error_shown(), \
        "Login error was displayed"


def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in(VALID_EMAIL, INVALID_PASSWORD)

    assert login_page.is_password_error_shown(), \
        "Password error was not displayed"


def test_login_invalid_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in(INVALID_EMAIL, VALID_PASSWORD)

    assert login_page.is_email_error_shown(), \
        "Email validation error was not displayed"


def test_login_unregistered_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in(UNREGISTERED_EMAIL, VALID_PASSWORD)

    assert login_page.is_no_customer_error_shown(), \
        "No customer account error was not displayed"


def test_login_empty_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in("", VALID_PASSWORD)

#     assert login_page.is_email_error_shown(), \
#         "Email validation error was not displayed"
    assert login_page.is_no_customer_error_shown(), \
        "No customer account error was not displayed"


def test_login_empty_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in(VALID_EMAIL, "")

    assert login_page.is_login_error_shown(), \
        "Login error was not displayed"


def test_login_empty_email_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.log_in("", "")

    assert login_page.is_login_error_shown(), \
        "Login error was not displayed"