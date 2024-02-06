
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('lastBird@gmail.com')

    def go_to_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('102401')

    def go_to_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

    def find_profile(self):
        profile = self.browser.find_element(*LoginPageLocators.PROFILE)
        return profile

    def go_to_invalid_email(self):
        invalid_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        invalid_email.send_keys('lolBird@gmail2@.by46')

    def go_to_error(self):
        error = self.browser.find_element(*LoginPageLocators.ERROR)
        return error
