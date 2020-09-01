from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    
class LoginPageLocators():
    REGISTER_FORM = (By.ID, 'register_form') 
    LOGIN_FORM = (By.ID,'login_form')
    REGISTER_EMAIL_FIELD = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    ADD_PRODUCT_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NOW_BUSKET = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')

class BasketPageLocators():
    ADDED_PRODUCT_LIST = (By.ID, 'basket_formset')
    EMPTY_BASKET_MESSAGE = (By.ID, 'content_inner')