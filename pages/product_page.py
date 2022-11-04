from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*Locators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def take_product_name(self):
        # product_name = self.browser.find_element(*Locators.PRODUCT_NAME)
        return self.browser.find_element(*Locators.PRODUCT_NAME).text

    def take_product_price(self):
        # product_price = self.browser.find_element(*Locators.PRODUCT_PRICE)
        return self.browser.find_element(*Locators.PRODUCT_PRICE).text

    def should_be_correct_product_name(self, product_name):
        # print(product_name)
        basket_product_name = self.browser.find_element(*Locators.BASKET_PRODUCT_NAME).text
        assert basket_product_name == product_name, f"Incorrect product name representation."

    def should_be_correct_product_price(self, product_price):
        # print(product_price)
        basket_product_price = self.browser.find_element(*Locators.BASKET_PRODUCT_PRICE).text
        assert basket_product_price == product_price, f"Incorrect product price representation."
