import time
import requests as requests
from pages.login_page import LoginPage


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_login_button()
    browser.implicitly_wait(5)
    response = requests.get('http://34.141.58.52:8080/#/profile')
    assert response.status_code == 200
    browser.save_screenshot('login_done.png')


def test_invalid_email(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_invalid_email()
    time.sleep(2)
    page.go_to_password()
    page.go_to_login_button()
    time.sleep(2)
    browser.save_screenshot('result_test_invalid_email.png')
    error = page.go_to_error()
    assert error
