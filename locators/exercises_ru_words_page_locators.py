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
    PAGE_LIST1 = (By.XPATH, '//ul[@aria-label="Breadcrumbs"]//a')
    PAGE_LIST1_1 = (By.XPATH, '(//ul[@aria-label="Breadcrumbs"]//a)[1]')
    PAGE_LIST1_2 = (By.XPATH, '(//ul[@aria-label="Breadcrumbs"]//a)[2]')
    PAGE_LIST1_3 = (By.XPATH, '(//ul[@aria-label="Breadcrumbs"]//a)[3]')
    PAGE_LIST2 = (By.XPATH, "//aside//button")
    PAGE_LIST2_3 = (By.XPATH, "(//aside//button)[3]")
    PAGE_LIST3 = (By.XPATH, '//div[contains(@class, "series-page")]//a')
    PAGE_LIST3_1 = (By.XPATH, '(//div[contains(@class, "series-page")]//a)[1]')
    PAGE_LIST3_2 = (By.XPATH, '(//div[contains(@class, "series-page")]//a)[2]')
    PAGE_LIST3_3 = (By.XPATH, '(//div[contains(@class, "series-page")]//a)[3]')
    PAGE_LIST3_4 = (By.XPATH, '(//div[contains(@class, "series-page")]//a)[4]')
    # PAGE_LIST3 = (By.XPATH, "//main//div/a")
    CARD_IMAGES_LIST4 = (By.XPATH, '//div[contains(@style, "svg")]')
