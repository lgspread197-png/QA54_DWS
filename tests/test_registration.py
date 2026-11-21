import uuid

from pages import registration_page
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By


VALID_GENDER = "Male"
VALID_FIRST_NAME = "Vladimir"
VALID_LAST_NAME = "VladimirVV"

VALID_EMAIL = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

VALID_PASSWORD = "Manuel12345$"
CONFIRM_PASSWORD = "Manuel12345$"

INVALID_EMAIL = "manuelgmail.com"
INVALID_PASSWORD = "123"
MISMATCH_PASSWORD = "Another123$"

EXISTING_EMAIL = "manuel11@gmail.com"

#
# def test_registration_success(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_page()
#     registration_page.fill_gender(VALID_GENDER)
#     registration_page.fill_first_name(VALID_FIRST_NAME)
#     registration_page.fill_last_name(VALID_LAST_NAME)
#     registration_page.fill_email_field(VALID_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.fill_password_confirmation_field(CONFIRM_PASSWORD)
#     registration_page.click_on_registration_button()
#
#     assert registration_page.is_registration_info_displayed(), \
#         "Registration was not successful"
#
# def test_registration_with_invalid_email(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_page()
#     registration_page.fill_gender(VALID_GENDER)
#     registration_page.fill_first_name(VALID_FIRST_NAME)
#     registration_page.fill_last_name(VALID_LAST_NAME)
#     registration_page.fill_email_field(INVALID_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.fill_password_confirmation_field(CONFIRM_PASSWORD)
#
#     error = registration_page.get_email_error()
#
#     assert "Wrong email" in error
#
# def test_registration_with_invalid_password(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_first_name(VALID_FIRST_NAME)
#     registration_page.fill_last_name(VALID_LAST_NAME)
#     registration_page.fill_email_field(VALID_EMAIL)
#     registration_page.fill_password_field(INVALID_PASSWORD)
#     registration_page.fill_password_confirmation_field(CONFIRM_PASSWORD)
#
#     error = registration_page.get_password_error()
#
#     assert "The password should have at least 6 characters." in error
#
# def test_registration_with_confirm_password(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_first_name(VALID_FIRST_NAME)
#     registration_page.fill_last_name(VALID_LAST_NAME)
#     registration_page.fill_email_field(VALID_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.fill_password_confirmation_field(MISMATCH_PASSWORD)
#
#     registration_page.click_on_registration_button()
#
#     error = registration_page.get_confirm_password_error()
#
#     assert "The password and confirmation password do not match." in error
#
#
# def test_registration_existed_user(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_page()
#     registration_page.fill_gender(VALID_GENDER)
#     registration_page.fill_first_name(VALID_FIRST_NAME)
#     registration_page.fill_last_name(VALID_LAST_NAME)
#     registration_page.fill_email_field(EXISTING_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.fill_password_confirmation_field(CONFIRM_PASSWORD)
#     registration_page.click_on_registration_button()
#
#     registration_page.click_on_registration_button()
#
#     error = registration_page.get_existed_email_error()
#
#     assert "The specified email already exists" in error


def fill_registration_form(
        registration_page,
        email,
        password,
        confirm_password,
        first_name=VALID_FIRST_NAME,
        last_name=VALID_LAST_NAME,
        gender=VALID_GENDER
):
    registration_page.open_registration_page()

    if gender is not None:
        registration_page.fill_gender(gender)

    registration_page.fill_first_name(first_name)
    registration_page.fill_last_name(last_name)
    registration_page.fill_email_field(email)
    registration_page.fill_password_field(password)
    registration_page.fill_password_confirmation_field(confirm_password)

    registration_page.click_on_registration_button()



def test_registration_invalid_email(driver):
    registration_page = RegistrationPage(driver)

    fill_registration_form(
        registration_page,
        INVALID_EMAIL,
        VALID_PASSWORD,
        VALID_PASSWORD
    )

    error = registration_page.get_field_error(
        registration_page.EMAIL_ERROR
    )

    assert "Wrong email" in error


def test_registration_short_password(driver):
    registration_page = RegistrationPage(driver)

    email = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

    fill_registration_form(
        registration_page,
        email,
        INVALID_PASSWORD,
        INVALID_PASSWORD
    )

    error = registration_page.get_field_error(
        registration_page.PASSWORD_ERROR
    )

    assert "at least 6 characters" in error



def test_registration_passwords_do_not_match(driver):
    registration_page = RegistrationPage(driver)

    email = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

    fill_registration_form(
        registration_page,
        email,
        VALID_PASSWORD,
        MISMATCH_PASSWORD
    )

    error = registration_page.get_field_error(
        registration_page.CONFIRM_PASSWORD_ERROR
    )

    assert "do not match" in error


def test_registration_existing_user(driver):
    registration_page = RegistrationPage(driver)

    fill_registration_form(
        registration_page,
        EXISTING_EMAIL,
        VALID_PASSWORD,
        VALID_PASSWORD
    )

    error = registration_page.get_validation_summary()

    assert "already exists" in error.lower()


def test_registration_empty_form(driver):
    registration_page = RegistrationPage(driver)

    fill_registration_form(
        registration_page,
        "",
        "",
        "",
        first_name="",
        last_name="",
        gender=None
    )

    first_name_error = registration_page.get_field_error(
        registration_page.FIRST_NAME_ERROR
    )

    last_name_error = registration_page.get_field_error(
        registration_page.LAST_NAME_ERROR
    )

    email_error = registration_page.get_field_error(
        registration_page.EMAIL_ERROR
    )

    password_error = registration_page.get_field_error(
        registration_page.PASSWORD_ERROR
    )

    assert first_name_error != ""
    assert last_name_error != ""
    assert email_error != ""
    assert password_error != ""


def test_registration_without_first_name(driver):
    registration_page = RegistrationPage(driver)

    fill_registration_form(
        registration_page,
        VALID_EMAIL,
        VALID_PASSWORD,
        VALID_PASSWORD,
        first_name=""
    )

    error = registration_page.get_field_error(
        registration_page.FIRST_NAME_ERROR
    )

    assert error != ""


def test_registration_without_last_name(driver):
    registration_page = RegistrationPage(driver)

    email = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

    fill_registration_form(
        registration_page,
        email,
        VALID_PASSWORD,
        VALID_PASSWORD,
        last_name=""
    )

    error = registration_page.get_field_error(
        registration_page.LAST_NAME_ERROR
    )

    assert error != ""


def test_registration_without_email(driver):
    registration_page = RegistrationPage(driver)

    fill_registration_form(
        registration_page,
        "",
        VALID_PASSWORD,
        VALID_PASSWORD
    )

    error = registration_page.get_field_error(
        registration_page.EMAIL_ERROR
    )

    assert error != ""


def test_registration_without_password(driver):
    registration_page = RegistrationPage(driver)

    email = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

    fill_registration_form(
        registration_page,
        email,
        "",
        ""
    )

    error = registration_page.get_field_error(
        registration_page.PASSWORD_ERROR
    )

    assert error != ""


def test_registration_without_confirm_password(driver):
    registration_page = RegistrationPage(driver)

    email = f"manuel_{uuid.uuid4().hex[:8]}@gmail.com"

    fill_registration_form(
        registration_page,
        email,
        VALID_PASSWORD,
        ""
    )

    error = registration_page.get_field_error(
        registration_page.CONFIRM_PASSWORD_ERROR
    )

    assert error != ""


