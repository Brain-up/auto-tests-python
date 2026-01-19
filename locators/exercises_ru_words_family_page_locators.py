"""Locators of web elements on the exercises subgroup "Family" page in the series "Words" on the "ru" local"""
from selenium.webdriver.common.by import By


class ExercisesRuWordsFamilyPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*")
    PAGE_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*")
    PAGE_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*")
    PAGE_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*")
    PAGE_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*")
    PAGE_SEVENTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*")
    PAGE_EIGHTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*/*")
    PAGE_NINTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*/*/*")
    PAGE_TENTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*/*/*/*")
    PAGE_ELEVENTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*/*/*/*/*/*")
