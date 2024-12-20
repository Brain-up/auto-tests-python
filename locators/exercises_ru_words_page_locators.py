"""Locators of web elements on the 'Exercises "Words"' page on the 'ru' local"""
from selenium.webdriver.common.by import By


class ExercisesRuWordsPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*")
    PAGE_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*")
    PAGE_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*")
    PAGE_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*")
    PAGE_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*")
    PAGE_SEVENTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*")
    PAGE_LIST1 = (By.XPATH, '//ul[@aria-label="Breadcrumbs"]/li')
    # PAGE_LIST1 = (By.XPATH, "//main//div/li")
    PAGE_LIST2 = (By.XPATH, "//aside//li")
    PAGE_LIST3 = (By.XPATH, '//div[contains(@class, "series-page")]//a')
    # PAGE_LIST3 = (By.XPATH, "//main//div/a")
    CARD_IMAGES_LIST4 = (By.XPATH, '//div[contains(@style, "svg")]')


class HeaderLocators:
    RU_BUTTON = (By.XPATH, "(//span/button)[1]")
