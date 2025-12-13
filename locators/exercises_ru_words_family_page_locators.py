"""Locators of web elements on the exercises subgroup "Family" page in the series "Words" on the "ru" local"""
from selenium.webdriver.common.by import By


class ExercisesRuWordsFamilyPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*")
