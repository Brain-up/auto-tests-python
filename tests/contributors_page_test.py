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

        @allure.title("Verify the composition and visibility of elements "
                      "on the 1st, 2nd, 3rd, 4th levels of nesting in the section")
        def test_cnp_01_03_verify_section_structure_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            structure_of_section = page.get_structure_of_section()
            visibility_of_subsections_on_the_1st_level = page.check_visibility_of_elements_in_section()
            structure_of_1st_level_subsection = page.get_structure_of_1st_level_in_section()
            visibility_of_subsections_on_1st_level = page.check_visibility_of_elements_in_subsections()
            structure_of_2nd_level_subsections = page.get_structure_of_2nd_level_in_section()
            visibility_of_elements_on_2nd_level = page.check_visibility_of_elements_on_2nd_level_in_section()
            structure_of_3rd_level_subsections = page.get_structure_of_3rd_level_in_section()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section()
            structure_of_4th_level_subsections = page.get_structure_of_4th_level_in_section()
            visibility_of_elements_on_4th_level = page.check_visibility_of_elements_on_4th_level_in_section()
            assert structure_of_section, "The section is empty"
            assert visibility_of_subsections_on_the_1st_level, "1th-level subsections are invisible on the page"
            assert structure_of_1st_level_subsection, "Subsections on the 1st level in the section are empty"
            assert visibility_of_subsections_on_1st_level, "1st-level subsections are invisible on the page"
            assert structure_of_2nd_level_subsections, "Elements on the 2nd level in the section are empty"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible on the page"
            assert structure_of_3rd_level_subsections, "Elements on the 3rd level in the section are empty"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"
            assert structure_of_4th_level_subsections, "Elements on the 4th level in the section are empty"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible on the page"

        @allure.title("Verify amount of contributor cards with images, links and descriptions in the section grid")
        def test_cnp_01_04_verify_structure_of_grid_in_section(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            amount_of_cards = page.get_amount_of_cards_in_the_grid()
            amount_of_images = page.get_amount_of_images_in_the_grid()
            amount_of_links = page.get_amount_of_links_in_the_grid()
            amount_of_descriptions = page.get_amount_of_descriptions_in_the_grid()
            assert amount_of_cards == ContributorsPageData.amount_of_cards_in_grid, \
                "The amount of contributor cards in the grid does not match the expected value"
            assert amount_of_images == ContributorsPageData.amount_of_images_in_section, \
                "The amount of images in the grid does not match the expected value"
            assert amount_of_links == ContributorsPageData.amount_of_links_in_section, \
                "The amount of links in the grid does not match the expected value"
            assert amount_of_descriptions == ContributorsPageData.amount_of_descriptions_in_grid, \
                "The amount of descriptions in the grid does not match the expected value"
