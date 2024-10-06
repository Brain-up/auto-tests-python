"""Auto tests for verifying web elements on the 'Groups' page"""
import allure
import pytest
from pages.groups_page import GroupsPage


@pytest.mark.skip(reason="unsupported preconditions")
@allure.epic("The Groups Page")
class TestGroupsPage:
    class TestGroupsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_gp_01_01_verify_page_presence_and_visibility(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"
