import time
import pytest
from pages.main_page import MainPage


class TestMainPage:

    def test_MP_01_verify_redirection_to_description_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_description_page()

    def test_MP_02_verify_redirection_to_telegram_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_telegram_page()

    def test_MP_03_verify_redirection_to_donate_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_donate_page()

    def test_MP_04_verify_redirection_to_contacts_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_contacts_page()

    # @pytest.mark.xfail
    def test_MP_05_verify_redirection_to_specialists_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_specialists_page()

    def test_MP_06_verify_redirection_to_github(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_github()

    # @pytest.mark.xfail
    def test_MP_07_verify_redirection_to_contributors_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_contributors_page()

    def test_MP_08_verify_redirection_to_used_resources_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_used_resources_page()
