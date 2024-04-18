"""Locators of web elements on the starting page for unauthorized users"""
from selenium.webdriver.common.by import By


class StartUnauthorizedPageLocators:
    SECTION_1_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*")
    SECTION_1_SECOND_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*/*")
    SECTION_1_THIRD_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*/*/*")
    SECTION_1_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*/*/*/*")
    SECTION_2_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*")
    SECTION_2_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'm-auto')]/*")
    SECTION_2_THIRD_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*//*//*")
    UNAUTH_START_PAGE_CONTENT = (By.TAG_NAME, "main")
    UNAUTH_START_PAGE_SECTIONS = (By.TAG_NAME, "section")
    UNAUTH_START_PAGE_SECTION_1_TEXT = (By.XPATH, "//p[contains(@class, 'text')]")
    UNAUTH_START_PAGE_SECTION_2_TEXT = (By.XPATH, "//div[contains(@class, 'font')]")
    UNAUTH_START_PAGE_TITLES = (By.XPATH, "//h2")
    UNAUTH_START_PAGE_SUBTITLES = (By.XPATH, "//h4")
