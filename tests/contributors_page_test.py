"""Auto tests for verifying web elements on the 'Contributors' page"""
import allure
from pages.contributors_page import ContributorsPage
from test_data.contributors_page_data import ContributorsPageData


@allure.epic("The Contributors Page")
class TestContributorsPage:
    class TestContributorsPageStructure:

        @allure.title("Verify presence, visibility and structure of content on the page")
        def test_cnp_01_01_verify_page_presence_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            print(driver.current_url)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            structure_of_page = page.get_structure_of_page()
            visibility_of_elements_on_the_1st_level = page.check_visibility_of_elements_on_page()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"
            assert structure_of_page, "The page is empty"
            assert visibility_of_elements_on_the_1st_level, "1th-level elements are invisible on the page"

        @allure.title("Verify amount and visibility of sections with content on the page")
        def test_cnp_01_02_verify_sections_structure_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            sections_amount = page.get_amount_of_sections_on_page()
            sections_visibility = page.check_visibility_of_sections()
            assert sections_amount == ContributorsPageData.amount_of_sections_with_content_on_page, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible on the page"

        @allure.title("Verify the composition and visibility of elements on the 1st level of nesting in the section")
        def test_cnp_01_03_verify_section_structure_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            structure_of_section_1 = page.get_structure_of_section()
            visibility_of_elements_on_the_1st_level = page.check_visibility_of_elements_in_section()
            assert structure_of_section_1, "The section 1 is empty"
            assert visibility_of_elements_on_the_1st_level, "1th-level elements are invisible on the page"
