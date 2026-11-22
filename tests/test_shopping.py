
from pages.shopping_page import ShoppingPage
from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_adding_success(driver):

    login_page = LoginPage(driver)    # Авторизация
    login_page.open_login_page()
    login_page.log_in("manuel11@gmail.com", "Manuel12345$")

    shopping_page = ShoppingPage(driver)    # Добавление товара в корзину
    shopping_page.click_page_button()
    shopping_page.click_add_to_cart()
    shopping_page.open_shop_cart()

    shopping_page.set_quantity(1)    # Устанавливаем количество товара
    shopping_page.click_update_cart()

    assert shopping_page.get_quantity() == "1"    # проверяет количество товара в корзине

    shopping_page.fill_check_box()    # Переход к оформлению заказа
    shopping_page.checkout_button()

    elements = driver.find_elements(
        By.XPATH, "//*[contains(., 'Billing Address')]"
    )

    for element in elements:
        if element.text.strip() == "Billing Address":
            print(element.tag_name)
            print(element.is_displayed())
            print(element.get_attribute("outerHTML"))

    assert shopping_page.is_page_redirected("/onepagecheckout")
    print(driver.find_element(By.TAG_NAME, "body").text)
    assert shopping_page.is_billing_address_displayed()

    shopping_page.select_billing_new_address("New Address")    # Заполнение Billing Address
    shopping_page.select_billing_country("Israel")
    shopping_page.fill_billing_city("Haifa")
    shopping_page.fill_billing_address1("Ben Gurion 1")
    shopping_page.fill_postal_code("1234567")
    shopping_page.fill_phone_number("0531112233")

    shopping_page.click_billing_button_continue()

    shopping_page.click_shipping_address_button()    # Подтверждение Shipping Address

    shopping_page.choose_shipping_method_ground()    # Выбор способа доставки
    shopping_page.click_shipping_method_button()

    shopping_page.wait_for_next_step()

    assert shopping_page.is_payment_method_displayed()

    shopping_page.choose_payment_cash_on_delivery()    # Выбор способа оплаты Cash On Delivery
    shopping_page.click_payment_method_button()

    shopping_page.wait_for_next_step()

    shopping_page.click_payment_info_button()    # Переход к Payment Information

    shopping_page.wait_for_next_step()

    shopping_page.click_confirm_order()    # Подтверждение заказа

    assert shopping_page.get_order_completed_message() == (
        "Your order has been successfully processed!")
