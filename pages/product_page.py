from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        add_product_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON)
        add_product_to_cart_button.click()

    def should_be_message_product_added_to_cart(self):
        product_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name_el.text
        message_product_added_to_cart_el = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        message_product_added_to_cart = message_product_added_to_cart_el.text
        
        assert product_name == message_product_added_to_cart, 'Name of product is not in message'
        
    def should_be_correct_price_of_cart(self):
        price_of_cart_el = self.browser.find_element(*ProductPageLocators.NOW_BUSKET)
        price_of_cart = price_of_cart_el.text
        price_of_added_product_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_of_added_product = price_of_added_product_el.text

        assert price_of_cart == price_of_added_product, 'Price of cart is not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but didn't"
            