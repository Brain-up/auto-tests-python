"""Locators of web elements in the Footer"""
from selenium.webdriver.common.by import By


class FooterLocators:
    FOOTER = (By.TAG_NAME, "footer")
    FOOTER_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//footer/*")
    FOOTER_SECOND_LEVEL_ELEMENTS = (By.XPATH, "//footer/*/*")
    FOOTER_THIRD_LEVEL_ELEMENTS = (By.XPATH, "//footer/*/*/*")
    FOOTER_FOURTH_LEVEL_ELEMENTS = (By.XPATH, "//footer/*/*/*/*")
    FOOTER_FIFTH_LEVEL_ELEMENTS = (By.XPATH, "//footer/*/*/*/*/*")
    FOOTER_SIXTH_LEVEL_ELEMENTS = (By.XPATH, "//footer/*/*/*/*/*/*")
    FOOTER_SEVENTH_LEVEL_ELEMENTS = (By.XPATH, "//footer/*/*/*/*/*/*/*")
    FOOTER_IMAGES = (By.XPATH, "//footer//img")
    FOOTER_LINKS = (By.XPATH, "//footer//a")
    FOOTER_TEXT = (By.XPATH, "//span[@data-test-support-message]")
    CONTACT_US_LINK = (By.XPATH, "//footer//a[@title]")
    JETBRAINS_IMAGE = (By.XPATH, "(//footer//li)[1]//img")
    SUPPORTER_LINKS = (By.XPATH, "//footer//li/a")
    WITH_THE_SUPPORT_TEXT = (By.XPATH, "//span[@data-test-support-message]")
