"""Auto tests for verifying web elements on the 'Contacts' page"""
import allure
from pages.contacts_page import ContactsPage
from test_data.contacts_page_data import ContactsPageData


@allure.epic("The Contacts Page")
class TestContactsPage:
    class TestContactsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_cp_01_01_verify_page_presence_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify the composition and visibility of elements on the 1st level of nesting in the section 1")
        def test_cp_01_02_verify_section1_structure_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level_in_section1()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_section1()
            assert structure_of_1st_level, "The section 1 is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-5th levels of nesting in the section 2""")
        def test_cp_01_03_verify_section2_structure_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level_in_section2()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_section2()
            structure_of_2nd_level = page.get_structure_of_2nd_level_in_section2()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_section2()
            structure_of_3rd_level = page.get_structure_of_3rd_level_in_section2()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section2()
            structure_of_4th_level = page.get_structure_of_4th_level_in_section2()
            visibility_of_elements_on_4th_level = page.check_visibility_of_elements_on_4th_level_in_section2()
            structure_of_5th_level = page.get_structure_of_5th_level_in_section2()
            visibility_of_elements_on_5th_level = page.check_visibility_of_elements_on_5th_level_in_section2()
            assert structure_of_1st_level, "The section 2 is empty"
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
            assert structure_of_2nd_level, "Subsections on the 2nd level in the section 2 are empty"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level in the section 2 are empty"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level in the section 2 are empty"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
            assert structure_of_5th_level, "Elements on the 5th level in the section 2 are empty"
            assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"

        @allure.title("Verify presence and visibility of sections and the dividing line on the page")
        def test_cp_01_04_verify_page_structural_elements(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            structure_of_page = page.get_page_structure()
            structural_elements_visibility = page.check_visibility_of_structural_elements()
            sections_amount = page.get_amount_of_sections()
            sections_visibility = page.check_visibility_of_sections()
            dividing_line = page.check_presence_of_dividing_line()
            dividing_line_visibility = page.check_visibility_of_dividing_line()
            assert structure_of_page, "The page is empty"
            assert structural_elements_visibility, "Structural elements of the page are invisible"
            assert sections_amount == ContactsPageData.amount_of_sections, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible"
            assert dividing_line, "The dividing line is absent on the page"
            assert dividing_line_visibility, "The dividing line is invisible"

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

        @allure.title("Verify values of the text in sections 1, 2 on the page")
        def test_cp_02_03_verify_text_in_sections(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            text_value_in_sections = page.get_values_of_text_in_sections()
            assert text_value_in_sections in ContactsPageData.text_on_page, \
                "The text in sections does not match the valid options"

        @allure.title("Verify values of the text in links in sections 1, 2 on the page")
        def test_cp_02_04_verify_text_in_links(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            links_text = page.get_text_in_links_in_sections()
            assert links_text == ContactsPageData.links_text, "Text in links do not match the valid values"

    class TestContactsPageLinks:

        @allure.title("""Verify presence, visibility, clickability, href, prefix, status code 
        of links in sections 1, 2 on the page""")
        def test_cp_03_01_verify_links_in_sections(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            links_presence = page.get_list_of_links_in_sections()
            links_visibility = page.check_visibility_of_links_in_sections()
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            link_prefix = page.check_email_link_href()
            links_status_codes = page.get_links_status_codes()
            assert links_presence is not None, "The 'Contacts' links are absent in DOM"
            assert links_visibility, "Links are invisible on the page"
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"
            assert links_href == ContactsPageData.links_href, "Attributes 'href' of links do not match the valid values"
            assert link_prefix, "The attribute 'href' of the email link does not contain the proper prefix"
            assert links_status_codes == ContactsPageData.links_status_codes, \
                "Links status codes do not match the expected values"

        @allure.title("Verify that links in sections 1, 2 lead to the correct pages after click")
        def test_cp_03_02_verify_links_lead_to_the_correct_pages(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            new_tabs = page.click_on_links()
            assert new_tabs == ContactsPageData.links_tm_href, \
                "Links in sections 1, 2 lead to incorrect pages after click"
