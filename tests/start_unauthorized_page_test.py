"""Auto tests for verifying web elements on the starting page for unauthorized users"""
import allure
from pages.start_unauthorized_page import StartUnauthorizedPage
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData


@allure.epic("The Start Unauthorized Page")
class TestStartUnauthorizedPage:
    class TestStartUnauthorizedPageStructure:

        @allure.title("Verify presence and visibility of content on the page")
        def test_su_01_01_verify_page_structure(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"

        @allure.title("Verify structure and visibility of sections with content on the page")
        def test_su_01_02_verify_sections_visibility(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            page_structure = page.get_amount_of_sections_on_page()
            sections_visibility = page.check_visibility_of_sections()
            assert page_structure == StartUnauthorizedPageData.amount_of_sections_with_content_on_page, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible on the page"

    class TestStartUnauthorizedPageText:

        @allure.title("Verify presence, visibility and text accuracy of the title #1 on the page")
        def test_su_02_01_verify_title_01(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            title_01_presence = page.check_start_unauthorized_page_title_01_presence()
            title_01_visibility = page.check_start_unauthorized_page_title_01_visibility()
            title_01_content = page.get_content_of_title_01_on_start_unauthorized_page()
            assert title_01_presence is not None, "The element is absent in DOM"
            assert title_01_visibility, "The element is invisible on the page"
            assert (title_01_content in
                    StartUnauthorizedPageData.start_unauthorized_page_elements_content["page_title_1_content"]), \
                   "The content of the title #1 does not match the any of the valid option"

        @allure.title("Verify presence, visibility and content accuracy of the text #1 on the page")
        def test_su_02_02_verify_text_01(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            text_01_presence = page.check_start_unauthorized_page_text_01_presence()
            text_01_visibility = page.check_start_unauthorized_page_text_01_visibility()
            text_01_content = page.get_content_of_text_01_on_start_unauthorized_page()
            assert text_01_presence is not None, "The element is absent in DOM"
            assert text_01_visibility, "The element is invisible on the page"
            assert (text_01_content in
                    StartUnauthorizedPageData.start_unauthorized_page_elements_content["page_text_1_content"]), \
                   "The content of the text #1 does not match the any of the valid option"

