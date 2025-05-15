"""Auto tests for verifying web elements on the 'Contacts' page"""
import allure
from pages.contacts_page import ContactsPage as ctPage
from test_data.contacts_page_data import ContactsPageData as ctPD


@allure.epic("The Contacts Page")
class TestContactsPage:
    class TestContactsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_cp_01_01_verify_page_presence_and_visibility(self, driver, contacts_page_open):
            page = ctPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify the composition and visibility of elements on the 1st level of nesting in the section 1")
        def test_cp_01_02_verify_section1_structure_and_visibility(self, driver, contacts_page_open):
            page = ctPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level_in_section1()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_section1()
            assert structure_of_1st_level, "The section 1 is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-5th levels of nesting in the section 2""")
        def test_cp_01_03_verify_section2_structure_and_visibility(self, driver, contacts_page_open):
            page = ctPage(driver)
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

        @allure.title("Verify presence, visibility of sections, the dividing line and elements with text on the page")
        def test_cp_01_04_verify_page_structural_elements(self, driver, contacts_page_open):
            page = ctPage(driver)
            structure_of_page = page.get_page_structure()
            structural_elements_visibility = page.check_visibility_of_structural_elements()
            sections_amount = page.get_amount_of_sections()
            sections_visibility = page.check_visibility_of_sections()
            dividing_line = page.check_presence_of_dividing_line()
            dividing_line_visibility = page.check_visibility_of_dividing_line()
            title = page.check_title_presence()
            title_visibility = page.check_title_visibility()
            subtitles = page.get_list_of_subtitles()
            subtitles_visibility = page.check_visibility_of_subtitles()
            elements_with_text = page.get_list_of_elements_with_text()
            elements_with_text_visibility = page.check_visibility_of_elements_with_text()
            assert structure_of_page, "The page is empty"
            assert structural_elements_visibility, "Structural elements of the page are invisible"
            assert sections_amount == ctPD.amount_of_sections, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible"
            assert dividing_line, "The dividing line is absent on the page"
            assert dividing_line_visibility, "The dividing line is invisible"
            assert title, "The title is absent on the page"
            assert title_visibility, "The title is invisible"
            assert subtitles, "Subtitles are absent on the page"
            assert subtitles_visibility, "Subtitles are invisible"
            assert elements_with_text, "Elements with text are absent on the page"
            assert elements_with_text_visibility, "Elements with text are invisible"

    class TestContactsPageText:
        @allure.title("Verify value of the title of the tab")
        def test_cp_02_01_verify_tab_title(self, driver, contacts_page_open):
            page = ctPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in ctPD.tab_title, "The tab title mismatches the valid value"

        @allure.title("Verify values of the title and subtitles with tags h1, h2 on the page")
        def test_cp_02_02_verify_page_title_and_subtitles(self, driver, contacts_page_open):
            page = ctPage(driver)
            title_value = page.get_value_of_title()
            subtitle_values = page.get_values_of_subtitles()
            assert title_value, "The title value on the page is empty"
            assert title_value in ctPD.page_title, "The title on the page mismatches the valid value"
            assert subtitle_values, "Subtitle values on the page are empty"
            assert all(element in ctPD.page_subtitles for element in subtitle_values), "Subtitles mismatch valid values"

        @allure.title("Verify content of the text in the section 2")
        def test_cp_02_03_verify_page_text(self, driver, contacts_page_open):
            page = ctPage(driver)
            text_content = page.get_text_content_on_page()
            assert text_content, "The text content in the section 2 is empty"
            assert all(element in ctPD.text_on_page for element in text_content), "Text mismatches valid values"

        @allure.title("Verify text in links in the section 2")
        def test_cp_02_04_verify_text_in_links(self, driver, contacts_page_open):
            page = ctPage(driver)
            links_text = page.get_text_in_links()
            assert links_text, "Text in links is empty"
            assert all(element in ctPD.links_text for element in links_text), "Links text mismatches valid values"

    class TestContactsPageLinks:
        @allure.title("Verify presence, visibility, clickability, href, prefix, status code of links in the section 2")
        def test_cp_03_01_verify_links_in_section2(self, driver, contacts_page_open):
            page = ctPage(driver)
            links_presence = page.get_list_of_links()
            links_visibility = page.check_links_visibility()
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            link_prefix = page.check_email_link_href()
            links_status_codes = page.get_tm_links_status_codes()
            assert links_presence, "Links are absent on the page"
            assert links_visibility, "Links are invisible"
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"
            assert all(element in ctPD.links_href for element in links_href), \
                "Attributes 'href' of links mismatch valid values"
            assert link_prefix, "The attribute 'href' of the email link does not contain the proper prefix"
            assert all(element in ctPD.links_status_code for element in links_status_codes), \
                "Status codes of links in breadcrumbs mismatch valid values"

        @allure.title("Verify if links in the section 2 lead to the correct pages after clicking")
        def test_cp_03_02_verify_links_lead_to_the_correct_pages(self, driver, contacts_page_open):
            page = ctPage(driver)
            new_tabs_urls = page.click_on_links()
            assert all(element in ctPD.pages_urls for element in new_tabs_urls), \
                "Links in the section 2 lead to incorrect pages after clicking"

        @allure.title("Verify that the email link calls an email client")
        def test_cp_03_03_verify_email_link_calls_an_email_client(self, driver, contacts_page_open):
            page = ctPage(driver)
            page.click_email_link()
            assert True, "The email link does not call an email client"
