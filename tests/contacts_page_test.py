"""Auto tests for verifying web elements on the 'Contacts' page"""
import allure
from pages.contacts_page import ContactsPage
from test_data.contacts_page_data import ContactsPageData


@allure.epic("The Contacts Page")
class TestContactsPage:
    class TestContactsPageStructure:

        @allure.title("Verify presence, visibility and structure of content on the page")
        def test_cp_01_01_verify_page_presence_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
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
        def test_cp_01_02_verify_sections_structure_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            sections_amount = page.get_amount_of_sections_on_page()
            sections_visibility = page.check_visibility_of_sections()
            assert sections_amount == ContactsPageData.amount_of_sections_with_content_on_page, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible on the page"

        @allure.title("Verify the composition and visibility of elements on the 1st level of nesting in the section 1")
        def test_cp_01_03_verify_section_1_structure_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            structure_of_section_1 = page.get_structure_of_section_1()
            visibility_of_elements_on_the_1st_level = page.check_visibility_of_elements_in_section_1()
            assert structure_of_section_1, "The section 1 is empty"
            assert visibility_of_elements_on_the_1st_level, "1th-level elements are invisible on the page"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st, 2nd, 3rd, 4th, 5th levels of nesting in the section 2""")
        def test_cp_01_04_verify_section_2_structure_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            structure_of_section_2 = page.get_structure_of_section_2()
            visibility_of_subsections_on_the_1st_level = page.check_visibility_of_elements_in_section_2()
            structure_of_2nd_level_subsection = page.get_structure_of_2nd_level_in_section_2()
            visibility_of_subsections_in_2nd_level_subsection = (
                page.check_visibility_of_elements_in_subsection_in_section_2())
            structure_of_3rd_level_subsections = page.get_structure_of_3rd_level_in_section_2()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section_2()
            structure_of_4th_level_subsections = page.get_structure_of_4th_level_in_section_2()
            visibility_of_elements_on_4th_level = page.check_visibility_of_elements_on_4th_level_in_section_2()
            structure_of_5th_level_subsections = page.get_structure_of_5th_level_in_section_2()
            visibility_of_elements_on_5th_level = page.check_visibility_of_elements_on_5th_level_in_section_2()
            assert structure_of_section_2, "The section 2 is empty"
            assert visibility_of_subsections_on_the_1st_level, "1th-level subsections are invisible on the page"
            assert structure_of_2nd_level_subsection, "Subsections on the 2nd level in the section 2 are empty"
            assert visibility_of_subsections_in_2nd_level_subsection, "2nd-level subsections are invisible on the page"
            assert structure_of_3rd_level_subsections, "Elements on the 3rd level in the section 2 are empty"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"
            assert structure_of_4th_level_subsections, "Elements on the 4th level in the section 2 are empty"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible on the page"
            assert structure_of_5th_level_subsections, "Elements on the 5th level in the section 2 are empty"
            assert visibility_of_elements_on_5th_level, "5th-level elements are invisible on the page"

        @allure.title("Verify presence and visibility of the dividing line on the page")
        def test_cp_01_05_verify_presence_and_visibility_of_dividing_line(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            dividing_line_presence = page.check_presence_of_dividing_line()
            dividing_line_visibility = page.check_visibility_of_dividing_line()
            assert dividing_line_presence is not None, "The dividing line is absent in DOM"
            assert dividing_line_visibility, "The dividing line is invisible on the page"

    class TestContactsPageText:

        @allure.title("Verify value of title with tag 'h1' on the page")
        def test_cp_02_01_verify_title_on_the_page(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            title_value = page.get_value_of_title_on_the_page()
            assert title_value, "The title value on the page is empty"
            assert title_value in ContactsPageData.page_title, "The title on the page doesn't match the valid value"

        @allure.title("Verify values of subtitles with tag 'h2' on the page")
        def test_cp_02_02_verify_subtitles_on_the_page(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            subtitle_values = page.get_values_of_subtitles()
            assert subtitle_values, "Subtitle values on the page are empty"
            assert subtitle_values in ContactsPageData.page_subtitles, \
                "The subtitles on the 'Contacts' page do not match the valid values"
