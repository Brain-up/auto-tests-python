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

        @allure.title("Verify amount and visibility of sections with content on the page")
        def test_su_01_02_verify_sections_structure_and_visibility(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            sections_amount = page.get_amount_of_sections_on_page()
            sections_visibility = page.check_visibility_of_sections()
            assert sections_amount == StartUnauthorizedPageData.amount_of_sections_with_content_on_page, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible on the page"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st, 2nd, 3rd levels of nesting in the section 1""")
        def test_su_01_03_verify_section_1_structure_and_visibility(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            structure_of_section_1 = page.get_structure_of_section_1()
            visibility_of_subsections_on_the_1st_level = page.check_visibility_of_elements_in_section_1()
            structure_of_2nd_level_subsection = page.get_structure_of_subsection_in_section_1()
            visibility_of_subsections_in_2nd_level_subsection = (
                page.check_visibility_of_elements_in_subsection_in_section_1())
            structure_of_3rd_level_subsections = page.get_structure_of_3th_level_in_section_1()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3th_level_in_section_1()
            assert structure_of_section_1, "The section 1 is empty"
            assert visibility_of_subsections_on_the_1st_level, "1th-level subsections are invisible on the page"
            assert structure_of_2nd_level_subsection, "Subsections on the 2nd level in the section 1 are empty"
            assert visibility_of_subsections_in_2nd_level_subsection, "2nd-level subsections are invisible on the page"
            assert structure_of_3rd_level_subsections, "Elements on the 3rd level in the section 1 are empty"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st, 2nd, 3rd levels of nesting in the section 2""")
        def test_su_01_04_verify_section_2_structure_and_visibility(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            structure_of_section_2 = page.get_structure_of_section_2()
            visibility_of_subsections_on_the_1st_level = page.check_visibility_of_elements_in_section_2()
            structure_of_2nd_level_subsection = page.get_structure_of_subsection_in_section_2()
            visibility_of_subsections_in_2nd_level_subsection = (
                page.check_visibility_of_elements_in_subsection_in_section_2())
            structure_of_3rd_level_subsections = page.get_structure_of_3th_level_in_section_2()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3th_level_in_section_2()
            assert structure_of_section_2, "The section 2 is empty"
            assert visibility_of_subsections_on_the_1st_level, "1th-level subsections are invisible on the page"
            assert structure_of_2nd_level_subsection, "Subsections on the 2nd level in the section 2 are empty"
            assert visibility_of_subsections_in_2nd_level_subsection, "2nd-level subsections are invisible on the page"
            assert structure_of_3rd_level_subsections, "Elements on the 3rd level in the section 2 are empty"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"

    class TestStartUnauthorizedPageText:

        @allure.title("Verify values of titles with tag 'h2' on the page")
        def test_su_02_01_verify_titles_on_the_page(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            title_values = page.get_values_of_titles()
            assert title_values, "Title values on ghe page are empty"
            assert title_values in StartUnauthorizedPageData.titles_on_start_unauthorized_page, \
                "The titles on start unauthorized page do not match the valid values"

        @allure.title("Verify presence, visibility and text accuracy of the title #1 on the page")
        def test_su_02_02_verify_title_01(self, driver, main_page_open):
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
        def test_su_02_03_verify_text_01(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            text_01_presence = page.check_start_unauthorized_page_text_01_presence()
            text_01_visibility = page.check_start_unauthorized_page_text_01_visibility()
            text_01_content = page.get_content_of_text_01_on_start_unauthorized_page()
            assert text_01_presence is not None, "The element is absent in DOM"
            assert text_01_visibility, "The element is invisible on the page"
            assert (text_01_content in
                    StartUnauthorizedPageData.start_unauthorized_page_elements_content["page_text_1_content"]), \
                   "The content of the text #1 does not match the any of the valid option"

