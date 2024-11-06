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
    PAGE_LINK1 = (By.XPATH, "(//ol//a)[1]")
    PAGE_LINK2 = (By.XPATH, "(//ol//a)[2]")
    PAGE_LINKS = (By.XPATH, "//ol//a")
    # PAGE_TILES = (By.XPATH, "//ol/li")
    PAGE_TILES = (By.CSS_SELECTOR, ".list-item")
    PAGE_TITLE = (By.TAG_NAME, "h3")
    PAGE_SUBTITLES = (By.TAG_NAME, "h4")


class HeaderLocators:
    EN_BUTTON = (By.XPATH, "(//span/button)[2]")
    RU_BUTTON = (By.XPATH, "(//span/button)[1]")
