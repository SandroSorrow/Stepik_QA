from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        email_field.send_keys(email)
        pass1_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD1_FIELD)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2_FIELD)
        pass2_field.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
