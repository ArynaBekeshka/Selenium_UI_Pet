from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_like_pet(self):
        like_btn = self.browser.find_element(*MainPageLocators.LIKE_BTN)
        like_btn.click()

    def go_to_filter_by_pet_name(self):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        filter_by_pet_name.send_keys('ivan')
        filter_by_pet_name.send_keys(Keys.RETURN)

    def go_to_comment_pet(self):
        details_btn = self.browser.find_element(*MainPageLocators.DETAILS_BTN)
        details_btn.click()
        comment_field = self.browser.find_element(*MainPageLocators.COMMENT_FIELD)
        comment_field.send_keys('wow, ur pet awesome,Like!')
        save_btn = self.browser.find_element(*MainPageLocators.SAVE_BTN)
        save_btn.submit()
