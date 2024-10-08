"""Auto tests for verifying web elements on the 'Groups' page"""
import allure
import pytest
from pages.groups_page import GroupsPage


# @pytest.mark.skip(reason="unsupported preconditions")
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

        @allure.title("Verify composition, visibility of elements on the 1st-2nd levels of nesting on the page")
        def test_gp_01_02_verify_page_structure_and_visibility(self, driver, auto_test_user_authorized):
            page = GroupsPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level()
            assert structure_of_1st_level, "The page is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
