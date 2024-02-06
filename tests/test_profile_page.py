import time

from conftest import test_go_to_login
from pages.profile_page import ProfilePage


def test_go_to_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    browser.save_screenshot('result_profile_opened.png')


def test_go_to_create_new_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_create_pet_btn()
    page.go_to_pet_name()
    page.go_to_pet_type()
    page.go_to_cat_pet_type()
    page.go_to_age_field()
    page.go_to_gender_field()
    page.go_to_select_gender_pet()
    page.go_to_submit_btn()
    browser.implicitly_wait(2)
    page.go_to_choose_photo_btn()
    page. go_to_file_upload_btn()
    browser.implicitly_wait(3)
    browser.save_screenshot('result_pet_created.png')


def test_go_to_edit_type_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    browser.implicitly_wait(2)
    page.go_to_edit_btn()
    page.go_to_type_field()
    page.go_to_dog_type_edit()
    page.go_to_save_btn()
    time.sleep(2)
    browser.save_screenshot('result_edit_name.png')


def test_go_to_edit_name_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_name_pet()
    page.go_to_name_field_edit()
    page.go_to_save_btn_name()
    browser.implicitly_wait(2)
    browser.save_screenshot('result_edit_name.png')


def test_go_to_delete_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_pet_btn()
    page.go_to_yes_btn()
    time.sleep(2)
    browser.save_screenshot('result_delete_pet.png')


def test_go_to_delete_all_pets(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_all_pets()
    time.sleep(1)
    page.go_to_approval_btn()
    time.sleep(1)
    browser.save_screenshot('result_delete_all_pets.png')
