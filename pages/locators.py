from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")
    BASKET_LINK_INVALID = (By.ID, "basket_link_invalid")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form > button")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner > strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(2)")
