"""Locators of web elements on the 'Groups' page"""
from selenium.webdriver.common.by import By


class GroupsPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
    PAGE_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*")
    PAGE_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*")
    PAGE_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*")
    PAGE_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*")
    PAGE_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//main/*/*/*/*/*/*")
    PAGE_IMAGES = (By.XPATH, "//ol//img")
    PAGE_LINKS = (By.XPATH, "//ol//a")
    # PAGE_TILES = (By.XPATH, "//ol/li")
    PAGE_TILES = (By.CSS_SELECTOR, ".list-item")
    PAGE_TITLE = (By.TAG_NAME, "h3")
