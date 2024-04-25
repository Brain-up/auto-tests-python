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
            print(driver.current_url)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"

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
