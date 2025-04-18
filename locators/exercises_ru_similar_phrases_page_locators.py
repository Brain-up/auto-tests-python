"""Locators of web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
from selenium.webdriver.common.by import By


class ExercisesRuSimilarPhrasesPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*")
    PAGE_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*")
    PAGE_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*")
    PAGE_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*")
    PAGE_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*")
    PAGE_SEVENTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*")
    PAGE_LIST1 = (By.XPATH, '//ul[@aria-label="Breadcrumbs"]//a')
    PAGE_LIST2 = (By.XPATH, "//aside//button")
    PAGE_LIST3 = (By.XPATH, '//div[contains(@class, "series-page")]//a')
    CARD_IMAGES_LIST4 = (By.XPATH, '//div[contains(@style, "svg")]')
