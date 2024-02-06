import pytest
from selenium import webdriver
from pages.login_page import LoginPage

link = 'http://34.141.58.52:8080/#/login'


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_go_to_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_login_button()
