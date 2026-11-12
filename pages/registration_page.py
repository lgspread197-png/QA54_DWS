# логин \ пароль - manuel@gmail.com   Manuel12345$
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    REGISTRATION_LINK = (By.XPATH, "//a[normalize-space()='Register']")
    GENDERS = {
        "male": (By.ID, "gender-male"),
        "female": (By.ID, "gender-female"),
    }
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#LastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#Email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR,"#ConfirmPassword")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register-button")

    REGISTRATION_INFO = (By.CSS_SELECTOR, "div[class='header-links'] a[class='account']")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()

    def fill_gender(self):
        self.driver.find_element(*self.GENDERS).click()

    def fill_first_name(self, firstname):
        self.driver.find_element(*self.FIRST_NAME_INPUT).clear()
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(firstname)

    def fill_last_name(self, lastname):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(lastname)

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def fill_password_confirmation_field(self, confirm_password):
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).clear()
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(confirm_password)

    def click_on_registration_button(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION).click()

    # def is_sign_out_displayed(self):
    #     return self.driver.find_element(*self.SIGN_OUT_BUTTON).is_displayed()
    def is_registration_info_displayed(self):
        try:
            WebDriverWait(self.driver, timeout=10).until(
                expected_conditions.visibility_of_element_located(self.REGISTRATION_INFO)
            )
            return True
        except TimeoutException:
            return False

    # def get_alert_text(self):
    #     alert = WebDriverWait(self.driver, timeout=10).until(
    #         expected_conditions.alert_is_present()
    #     )
    #     return alert.text
    #
    # def accept_alert(self):
    #     self.driver.switch_to.alert.accept()