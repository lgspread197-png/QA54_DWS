# логин \ пароль - manuel11@gmail.com   Manuel12345$
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage(BasePage):
    REGISTRATION_LINK = (By.XPATH, "//a[normalize-space()='Register']")

    GENDERS = {
        "male": (By.ID, "gender-male"),
        "female": (By.ID, "gender-female"),
    }

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#LastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#ConfirmPassword")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register-button")

    REGISTRATION_INFO = (By.CSS_SELECTOR, "div.header-links a.account")

    "___________________________________"

    EMAIL_ERROR = (By.CSS_SELECTOR, "span[data-valmsg-for='Email']")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "span[data-valmsg-for='Password']")
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, "span[data-valmsg-for='ConfirmPassword']")
    EXISTED_EMAIL_ERROR = (By.CSS_SELECTOR, "div[class='validation-summary-errors'] ul li")
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, "span[data-valmsg-for='FirstName']")
    LAST_NAME_ERROR = (By.CSS_SELECTOR, "span[data-valmsg-for='LastName']")

    VALIDATION_SUMMARY = (By.CSS_SELECTOR, ".validation-summary-errors")


    # def __init__(self, driver):
    #     self.driver = driver

    def open_registration_page(self):
        # self.driver.find_element(*self.REGISTRATION_LINK).click()
        self.click(self.REGISTRATION_LINK)

    def fill_gender(self, gender):
        gender = gender.lower()

        if gender not in self.GENDERS:
            raise ValueError("Gender must be male or female")

        # self.driver.find_element(*self.GENDERS[gender]).click()
        self.click(self.GENDERS[gender])

    def fill_first_name(self, firstname):
        # self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        # self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(firstname)
        self.fill_text_input(self.FIRST_NAME_INPUT, firstname)

    def fill_last_name(self, lastname):
        # self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        # self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(lastname)
        self.fill_text_input(self.LAST_NAME_INPUT, lastname)

    def fill_email_field(self, email):
        # self.driver.find_element(*self.EMAIL_INPUT).clear()
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.fill_text_input(self.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        # self.driver.find_element(*self.PASSWORD_INPUT).clear()
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.fill_text_input(self.PASSWORD_INPUT, password)

    def fill_password_confirmation_field(self, confirm_password):
        # self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
        # self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)
        self.fill_text_input(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def click_on_registration_button(self):
        # self.driver.find_element(*self.BUTTON_REGISTRATION).click()
        self.click(self.BUTTON_REGISTRATION)

    def is_registration_info_displayed(self):
        # try:
        #     WebDriverWait(self.driver, timeout=10).until(
        #         EC.visibility_of_element_located(self.REGISTRATION_INFO)
        #     )
        #     return True
        # except TimeoutException:
        #     return False
        return self.is_element_shown(self.REGISTRATION_INFO)

    # def get_email_error(self):
    #     error = WebDriverWait(self.driver, timeout=10).until(
    #         expected_conditions.visibility_of_element_located(self.EMAIL_ERROR)
    #     )
    #     return error.text
    #
    # def get_password_error(self):
    #     error = WebDriverWait(self.driver, timeout=10).until(
    #         expected_conditions.visibility_of_element_located(self.PASSWORD_ERROR)
    #     )
    #     return error.text
    #
    # def get_confirm_password_error(self):
    #     error = WebDriverWait(self.driver, timeout=10).until(
    #         expected_conditions.visibility_of_element_located(self.CONFIRM_PASSWORD_ERROR)
    #     )
    #     return error.text
    #
    # def get_existed_email_error(self):
    #     error = WebDriverWait(self.driver, timeout=10).until(
    #         expected_conditions.visibility_of_element_located(self.EXISTED_EMAIL_ERROR)
    #     )
    #     return error.text

    def get_field_error(self, locator):
        # element = WebDriverWait(self.driver, timeout=10).until(
        #     EC.visibility_of_element_located(locator)
        # )
        # return element.text
        return self.get_element_text(locator)

    def get_validation_summary(self):
        # element = WebDriverWait(self.driver, timeout=10).until(
        #     EC.visibility_of_element_located(self.VALIDATION_SUMMARY)
        # )
        # return element.text
        return self.get_element_text(self.VALIDATION_SUMMARY)