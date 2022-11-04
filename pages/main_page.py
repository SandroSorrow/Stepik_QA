from .base_page import BasePage
from .locators import MainPageLocators as Locators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*Locators.LOGIN_PAGE)
        login_link.click()
        # для явного перехода на страницу login возвращаем PageObject:
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*Locators.LOGIN_PAGE), "Login link is not presented"

