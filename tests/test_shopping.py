import time

from pages.shopping_page import ShoppingPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_adding_success(driver):

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.log_in("manuel11@gmail.com","Manuel12345$")

    shopping_page = ShoppingPage(driver)

    shopping_page.click_page_button()
    shopping_page.click_add_to_cart()
    shopping_page.open_shop_cart()

    shopping_page.set_quantity(1)
    assert shopping_page.get_quantity() == "1"

    shopping_page.fill_check_box()
    shopping_page.checkout_button()

    assert shopping_page.is_page_redirected("/onepagecheckout")

    shopping_page.select_billing_new_address("New Address")
    shopping_page.select_billing_country("Israel")
    shopping_page.fill_billing_city("Haifa")
    shopping_page.fill_billing_address1("Ben Gurion 1")
    shopping_page.fill_postal_code("1234567")
    shopping_page.fill_phone_number("0531112233")

    shopping_page.click_billing_button_continue()
    time.sleep(1)
    assert shopping_page.is_element_shown("li[id='opc-shipping'] h2")
    shopping_page.click_shipping_address_button()
    time.sleep(8)
    assert shopping_page.is_element_shown("li[id='opc-shipping_method'] h2")
    shopping_page.choose_shipping_method_ground()
    time.sleep(1)
    assert shopping_page.is_element_shown("li[id='opc-payment_method'] h2")
    shopping_page.click_shipping_method_button()
    time.sleep(8)