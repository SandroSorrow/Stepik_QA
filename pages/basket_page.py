from .base_page import BasePage
from .locators import BasketPageLocators as Locators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*Locators.BASKET_SUMMARY), "No products in basket expected."

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*Locators.BASKET_SUMMARY), "Products in basket expected."

    def should_be_empty_basket_text_presented(self):
        empty_basket_text_localisation = [
            "Ваша корзина пуста Продолжить покупки",
            "Your basket is empty. Continue shopping",
        ]
        empty_basket_text = self.browser.find_element(*Locators.EMPTY_BASKET_TEXT).text
        assert empty_basket_text in empty_basket_text_localisation, "Empty basket text is not presented."

    def should_not_be_empty_basket_text_presented(self):
        assert self.is_not_element_present(*Locators.EMPTY_BASKET_TEXT), "Empty basket text is presented."
