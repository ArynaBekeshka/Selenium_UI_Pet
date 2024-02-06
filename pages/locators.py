from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    LIKE_BTN = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[8]/div/div[3]/div[2]')
    FILTER_BY_PET_NAME = (By.ID, 'petName')
    DETAILS_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[3]/div[1]/button[1]')
    COMMENT_FIELD = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div/div[3]/form/div/div/div[2]/div[1]')
    SAVE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/button[1]/span[2]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    PROFILE = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    ERROR = (By.CLASS_NAME, 'text-red-500')


class ProfilePageLocatorsCreateNewPet:
    CREATE_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    PET_NAME = (By.ID, 'name')
    PET_TYPE = (By.ID, 'typeSelector')
    CAT_PET_TYPE = (By.XPATH, '//*[@aria-label="cat"]')
    AGE_FIELD = (By.XPATH, '//*[@id="age"]/input')
    GENDER_FIELD = (By.ID, 'genderSelector')
    SELECT_GENDER_PET = (By.XPATH, '//*[@aria-label="Female"]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CHOOSE_PHOTO_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')
    FILE_UPLOAD_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > span')


class ProfilePageLocatorsEditNamePet:
    EDIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[5]/div/div[2]/button[1]')
    NAME_FIELD_EDIT = (By.CSS_SELECTOR, 'input#name')
    SAVE_BTN_NAME = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')


class ProfilePageLocatorsEditTypePet:
    EDIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[5]/div/div[2]/button[1]')
    TYPE_FIELD = (By.CSS_SELECTOR, '#typeSelector')
    DOG_TYPE_EDIT = (By.XPATH, '//*[@aria-label="dog"]')
    SAVE_BTN = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')


class ProfilePageLocatorsDeletePet:
    DELETE_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[5]/div/div[2]/button[2]')
    YES_BTN = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')


class ProfilePageLocatorsDeleteAllPets:
    DELETE_BTN2 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]')
    APPROVAL_BTN = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(3) > div:nth-of-type(2) > button')
