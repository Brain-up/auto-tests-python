"""Auto tests for verifying web elements in the Header of the site"""
import allure
from pages.header_page import HeaderPage


@allure.epic("Test Header")
class TestHeaderPage:
    class TestHeaderPageStructure:

        @allure.title("Verify presence and visibility of content in the Header")
        def test_hp_01_01_verify_page_presence_and_visibility(self, driver, main_page_open):
            page = HeaderPage(driver)
            page_content_presence = page.check_presence_of_header_content()
            page_content_visibility = page.check_visibility_of_header_content()
            assert page_content_presence is not None, "The Header content is absent in DOM"
            assert page_content_visibility, "The Header content is invisible on the page"
