"""Locators of web elements on the starting page for unauthorized users"""
from selenium.webdriver.common.by import By


class StartUnauthorizedPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_SECTIONS = (By.TAG_NAME, "section")
    PAGE_SUBTITLES = (By.XPATH, "//h4")
    PAGE_TITLES = (By.XPATH, "//h2")
    SECTION_1_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*")
    SECTION_1_IMAGE = (By.XPATH, "//section/img")
    SECTION_1_SECOND_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*/*")
    SECTION_1_TEXT = (By.XPATH, "//p[contains(@class, 'text')]")
    SECTION_1_THIRD_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*/*/*")
    SECTION_1_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "(//section)[1]/*/*/*/*")
    SECTION_2_FIRST_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*")
    SECTION_2_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//div[contains(@class, 'm-auto')]/*")
    SECTION_2_TEXT = (By.XPATH, "//div[contains(@class, 'font')]")
    SECTION_2_THIRD_LEVEL_ELEMENTS = (By.XPATH, "(//section)[2]/*//*//*")
