"""Locators of web elements on the 'Contributors' page"""
from selenium.webdriver.common.by import By


class ContributorsPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_STRUCTURE = (By.XPATH, "//main/*")
