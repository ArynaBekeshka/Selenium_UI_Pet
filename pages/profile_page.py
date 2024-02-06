
from .base_page import BasePage
from .locators import LoginPageLocators, ProfilePageLocatorsEditTypePet
from .locators import ProfilePageLocatorsCreateNewPet, ProfilePageLocatorsDeletePet
from .locators import ProfilePageLocatorsDeleteAllPets, ProfilePageLocatorsEditNamePet


class ProfilePage(BasePage):
    def go_to_profile_page(self):
        profile = self.browser.find_element(*LoginPageLocators.PROFILE)
        return profile

    def go_to_create_pet_btn(self):
        create_pet_btn = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.CREATE_PET_BTN)
        create_pet_btn.click()

    def go_to_pet_name(self):
        pet_name = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.PET_NAME)
        pet_name.send_keys('Janka')

    def go_to_pet_type(self):
        pet_type = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.PET_TYPE)
        pet_type.click()

    def go_to_cat_pet_type(self):
        cat_pet_type = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.CAT_PET_TYPE)
        cat_pet_type.click()

    def go_to_age_field(self):
        age_field = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.AGE_FIELD)
        age_field.send_keys('2')

    def go_to_gender_field(self):
        gender_field = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.GENDER_FIELD)
        gender_field.click()

    def go_to_select_gender_pet(self):
        select_gender_pet = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.SELECT_GENDER_PET)
        select_gender_pet.click()

    def go_to_submit_btn(self):
        submit_btn = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.SUBMIT_BTN)
        submit_btn.click()

    def go_to_choose_photo_btn(self):
        choose_photo_btn = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.CHOOSE_PHOTO_BTN)
        choose_photo_btn.send_keys(
            '//Users//arynabekeshko//PycharmProjects//Selenium_UI_Pet//pictures//pet_picture.png')

    def go_to_file_upload_btn(self):
        file_upload_btn = self.browser.find_element(*ProfilePageLocatorsCreateNewPet.FILE_UPLOAD_BTN)
        file_upload_btn.click()

    def go_to_edit_btn(self):
        edit_btn = self.browser.find_element(*ProfilePageLocatorsEditTypePet.EDIT_BTN)
        edit_btn.click()

    def go_to_type_field(self):
        type_field = self.browser.find_element(*ProfilePageLocatorsEditTypePet.TYPE_FIELD)
        type_field.click()

    def go_to_dog_type_edit(self):
        dog_type_edit = self.browser.find_element(*ProfilePageLocatorsEditTypePet.DOG_TYPE_EDIT)
        dog_type_edit.click()

    def go_to_save_btn(self):
        save_btn = self.browser.find_element(*ProfilePageLocatorsEditTypePet.SAVE_BTN)
        save_btn.submit()

    def go_to_edit_name_pet(self):
        edit_btn = self.browser.find_element(*ProfilePageLocatorsEditNamePet.EDIT_BTN)
        edit_btn.click()

    def go_to_name_field_edit(self):
        name_field_edit = self.browser.find_element(*ProfilePageLocatorsEditNamePet.NAME_FIELD_EDIT)
        name_field_edit.send_keys('Victor')

    def go_to_save_btn_name(self):
        save_btn_name = self.browser.find_element(*ProfilePageLocatorsEditNamePet.SAVE_BTN_NAME)
        save_btn_name.submit()

    def go_to_delete_pet_btn(self):
        delete_pet_btn = self.browser.find_element(*ProfilePageLocatorsDeletePet.DELETE_PET_BTN)
        delete_pet_btn.click()

    def go_to_yes_btn(self):
        yes_btn = self.browser.find_element(*ProfilePageLocatorsDeletePet.YES_BTN)
        yes_btn.click()

    def go_to_delete_all_pets(self):
        delete_btn2 = self.browser.find_element(*ProfilePageLocatorsDeleteAllPets.DELETE_BTN2)
        delete_btn2.click()

    def go_to_approval_btn(self):
        approval_btn = self.browser.find_element(*ProfilePageLocatorsDeleteAllPets.APPROVAL_BTN)
        approval_btn.click()
