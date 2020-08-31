from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):

    def no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_PRODUCT_LIST), \
            "Product list is found, but shouldn't be"
    
    def empty_basket_message(self):
        empty_basket_message_el = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        empty_basket_message = empty_basket_message_el.text

        assert 'Your basket is empty' in empty_basket_message, 'No message about empty basket found'

    
