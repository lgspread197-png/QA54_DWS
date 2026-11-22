from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ShoppingPage(BasePage):
    BASE_PAGE = (By.CSS_SELECTOR, "[alt='Tricentis Demo Web Shop']")
    ADD_TO_CART = (By.XPATH, "(//input[@value='Add to cart'])[2]")
    SHOP_CART = (By.CSS_SELECTOR, "[class='cart-label']")

    QTY_IN_CART = (By.XPATH, "//input[contains(@class, 'qty-input')]")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")

    AGREE_TERM_OF_USE_CHECK_BOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    BILLING_ADDRESS_HEADER = (By.CSS_SELECTOR, "#opc-billing h2")
    SELECT_BILLING_NEW_ADDRESS = (By.ID, "billing-address-select")
    SELECT_BILLING_COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    SELECT_BILLING_CITY = (By.ID, "BillingNewAddress_City")
    SELECT_BILLING_ADDRESS1 = (By.ID, "BillingNewAddress_Address1")
    SELECT_BILLING_POSTAL_CODE = (By.ID, "BillingNewAddress_ZipPostalCode")
    SELECT_BILLING_PHONE_NUMBER = (By.ID, "BillingNewAddress_PhoneNumber")

    BILLING_BUTTON_CONTINUE = (By.XPATH, "//input[@onclick='Billing.save()']")

    SHIPPING_ADDRESS_BUTTON = (By.XPATH, "//input[@onclick='Shipping.save()']")
    CHOOSE_SHIPPING_METHOD_GROUND = (By.CSS_SELECTOR, "label[for='shippingoption_0']")
    SHIPPING_METHOD_BUTTON = (By.CSS_SELECTOR, "input[class='button-1 shipping-method-next-step-button']")

    PAYMENT_METHOD_HEADER = (By.CSS_SELECTOR, "#opc-payment_method h2")
    PAYMENT_CASH_ON_DELIVERY = (By.ID, "paymentmethod_0")
    PAYMENT_METHOD_BUTTON_CONTINUE = (By.CSS_SELECTOR, "input.payment-method-next-step-button")

    PAYMENT_INFO_BUTTON_CONTINUE = (By.CSS_SELECTOR, "input.payment-info-next-step-button")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "input.confirm-order-next-step-button")
    ORDER_COMPLETED_MESSAGE = (By.CSS_SELECTOR, ".order-completed .title strong")

    def click_page_button(self):
        self.click(self.BASE_PAGE)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def open_shop_cart(self):
        self.click(self.SHOP_CART)

    def set_quantity(self, quantity):
        self.fill_text_input(self.QTY_IN_CART, quantity)

    def get_quantity(self):
        return self.driver.find_element(
            *self.QTY_IN_CART
        ).get_attribute("value")

    def click_update_cart(self):
        self.click(self.UPDATE_CART_BUTTON)

    def fill_check_box(self):
        self.click(self.AGREE_TERM_OF_USE_CHECK_BOX)

    def checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)

    def is_billing_address_displayed(self):
        return self.is_element_shown(self.BILLING_ADDRESS_HEADER)

    def select_billing_new_address(self, address):
        address_select = Select(
            self.driver.find_element(*self.SELECT_BILLING_NEW_ADDRESS)
        )
        address_select.select_by_visible_text(address)

    def select_billing_country(self, country):
        country_select = Select(
            self.driver.find_element(*self.SELECT_BILLING_COUNTRY)
        )
        country_select.select_by_visible_text(country)

    def fill_billing_city(self, city):
        self.fill_text_input(self.SELECT_BILLING_CITY, city)

    def fill_billing_address1(self, address1):
        self.fill_text_input(self.SELECT_BILLING_ADDRESS1, address1)

    def fill_postal_code(self, postal_code):
        self.fill_text_input(self.SELECT_BILLING_POSTAL_CODE, postal_code)

    def fill_phone_number(self, phone_number):
        self.fill_text_input(self.SELECT_BILLING_PHONE_NUMBER, phone_number)

    def click_billing_button_continue(self):
        self.click(self.BILLING_BUTTON_CONTINUE)

    def click_shipping_address_button(self):
        self.click(self.SHIPPING_ADDRESS_BUTTON)

    def choose_shipping_method_ground(self):
        self.click(self.CHOOSE_SHIPPING_METHOD_GROUND)

    def click_shipping_method_button(self):
        self.click(self.SHIPPING_METHOD_BUTTON)

    def choose_payment_cash_on_delivery(self):
        self.click(self.PAYMENT_CASH_ON_DELIVERY)

    def click_payment_method_button(self):
        self.click(self.PAYMENT_METHOD_BUTTON_CONTINUE)

    def is_payment_method_displayed(self):
        return self.is_element_shown(self.PAYMENT_METHOD_HEADER)

    def click_payment_info_button(self):
        self.click(self.PAYMENT_INFO_BUTTON_CONTINUE)

    def click_confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    def get_order_completed_message(self):
        return self.get_element_text(self.ORDER_COMPLETED_MESSAGE)

    def wait_for_next_step(self):
        WebDriverWait(self.driver, 15).until(
            lambda driver: "Loading next step..." not in
            driver.find_element(By.TAG_NAME, "body").text)