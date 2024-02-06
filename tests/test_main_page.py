from pages.main_page import MainPage


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result6.png')


def test_go_to_like_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_like_pet()
    browser.save_screenshot('result_liked_pet.png')


def test_go_to_filter_by_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    browser.save_screenshot('search_result.png')


def test_go_to_comment_pet(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_comment_pet()
    browser.save_screenshot('comment_result.png')

