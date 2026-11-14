import uuid

from pages.registration_page import RegistrationPage


VALID_GENDER = "Male"
VALID_FIRST_NAME = "Vladimir"
VALID_LAST_NAME = "VladimirVV"

VALID_EMAIL = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

VALID_PASSWORD = "Manuel12345$"
CONFIRM_PASSWORD = "Manuel12345$"

INVALID_EMAIL = "manuelgmail.com"
INVALID_PASSWORD = "123"


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_page()
    registration_page.fill_gender(VALID_GENDER)
    registration_page.fill_first_name(VALID_FIRST_NAME)
    registration_page.fill_last_name(VALID_LAST_NAME)
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.fill_password_confirmation_field(CONFIRM_PASSWORD)
    registration_page.click_on_registration_button()

    assert registration_page.is_registration_info_displayed(), \
        "Registration was not successful"

# def test_registration_with_invalid_email(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_email_field(INVALID_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.click_on_registration_button()
#
#     assert "Wrong email or password format" in registration_page.get_alert_text()
#     registration_page.accept_alert()
#
# def test_registration_with_invalid_password(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_email_field(VALID_EMAIL)
#     registration_page.fill_password_field(INVALID_PASSWORD)
#     registration_page.click_on_registration_button()
#
#     assert "Wrong email or password format" in registration_page.get_alert_text()
#     registration_page.accept_alert()
#
# def test_registration_existed_user(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_email_field("manuel@gmail.com")
#     registration_page.fill_password_field("Manuel12345$")
#     registration_page.click_on_registration_button()
#
#     assert registration_page.get_alert_text() == "User already exist"
#     registration_page.accept_alert()