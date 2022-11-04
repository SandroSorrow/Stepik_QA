from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")

    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner > strong")
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
