"""Auto tests for verifying web elements on the starting page for unauthorized users"""
import allure
from pages.start_unauthorized_page import StartUnauthorizedPage
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData


@allure.epic("The Start Unauthorized Page")
class TestStartUnauthorizedPage:

    @allure.title("Verify presence, visibility and text accuracy of the title #1 on the page")
    def test_su_01_01_verify_title_01(self, driver, main_page_open):
        page = StartUnauthorizedPage(driver)
        title_01_presence = page.check_start_unauthorized_page_title_01_presence()
        title_01_visibility = page.check_start_unauthorized_page_title_01_visibility()
        title_01_content = page.get_content_of_title_01_on_start_unauthorized_page()
        assert title_01_presence is not None, "The element is absent in DOM"
        assert title_01_visibility, "The element is absent in DOM"
        assert (title_01_content in
                StartUnauthorizedPageData.start_unauthorized_page_elements_content["page_title_1_content"]), \
               "The content of the title #1  does not match the any of the valid option"
