from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")
    BASKET_LINK_INVALID = (By.ID, "#basket_link_invalid")
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.ID, "#login_link_invalid")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "#basket_formset")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")

    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner > strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(2)")
