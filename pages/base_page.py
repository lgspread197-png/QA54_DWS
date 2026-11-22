from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    TIME_OUT: int = 10

    def __init__(self, driver):
        self.driver = driver

    def fill_text_input(self, locator, text):
        email_input = self.driver.find_element(*locator)
        email_input.clear()
        email_input.send_keys(text)

    # def click(self, locator):
    #     element = WebDriverWait(self.driver, self.TIME_OUT).until(
    #         expected_conditions.element_to_be_clickable(locator)
    #     )
    #     element.click()

    def click(self, locator):
        for attempt in range(3):
            try:
                element = WebDriverWait(self.driver, self.TIME_OUT).until(
                    expected_conditions.element_to_be_clickable(locator)
                )
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise

    # def click Ожидает, пока элемент станет видимым и доступным для нажатия.
    # Если во время работы страницы элемент обновился и Selenium потерял
    # ссылку на него (StaleElementReferenceException),
    # метод заново находит элемент и повторяет попытку клика.
    # Всего выполняется до 3 попыток. Если все попытки неудачны,
    # ошибка передаётся дальше.

    def is_element_shown(self, locator):
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                expected_conditions.visibility_of_element_located(locator)
            )

            return True
        except TimeoutException:
            return False


    def is_page_redirected(self, partial_url) -> bool:
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(
                expected_conditions.url_contains(partial_url)
            )

            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator) -> str | None:
        try:
            element = WebDriverWait(self.driver, self.TIME_OUT).until(
                expected_conditions.visibility_of_element_located(locator)
            )

            return element.text
        except TimeoutException:
            return None

    def clear(self):
        self.driver.delete_all_cookies()
