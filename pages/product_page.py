from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*Locators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def take_product_name(self):
        return self.browser.find_element(*Locators.PRODUCT_NAME).text

    def take_product_price(self):
        return self.browser.find_element(*Locators.PRODUCT_PRICE).text

    def should_be_correct_product_name(self, product_name):
        basket_product_name = self.browser.find_element(*Locators.BASKET_PRODUCT_NAME).text
        assert basket_product_name == product_name, "Incorrect product name presentation."

    def should_be_correct_product_price(self, product_price):
        basket_product_price = self.browser.find_element(*Locators.BASKET_PRODUCT_PRICE).text
        assert basket_product_price == product_price, "Incorrect product price presentation."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*Locators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*Locators.SUCCESS_MESSAGE), \
            "Success message has not disappear, but should be."
