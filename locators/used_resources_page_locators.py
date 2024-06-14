"""Locators of web elements on the 'Used Resources' page and related pages"""
from selenium.webdriver.common.by import By


class UsedResourcesPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*")
    PAGE_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*")
    PAGE_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*")
    PAGE_TEXT = (By.XPATH, "//section/p")
    SECTION_ICONS = (By.XPATH, "(//*[name()='svg'][@class])")
    SECTION_LINKS = (By.XPATH, "//section//a")
    TITLE_H1 = (By.TAG_NAME, "h1")
