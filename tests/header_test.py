"""Auto tests for verifying web elements in the Header of the site"""
import allure
from pages.header_page import HeaderPage


@allure.epic("Test Header")
class TestHeaderPage:
    class TestHeaderPageStructure:

        @allure.title("Verify presence and visibility of content in the Header")
        def test_hp_01_01_verify_header_presence_and_visibility(self, driver, main_page_open):
            page = HeaderPage(driver)
            page_content_presence = page.check_presence_of_header_content()
            page_content_visibility = page.check_visibility_of_header_content()
            assert page_content_presence is not None, "The Header content is absent in DOM"
            assert page_content_visibility, "The Header content is invisible on the page"

        @allure.title("Verify the composition and visibility of elements on the 1-6th levels of the Header")
        def test_hp_01_02_verify_header_structure_and_visibility(self, driver, main_page_open):
            page = HeaderPage(driver)
            structure_of_header = page.get_structure_of_1st_level_in_header()
            visibility_of_elements_on_the_1st_level = page.check_elements_visibility_on_1st_level_in_header()
            structure_of_2nd_level = page.get_structure_of_2nd_level_in_header()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_header()
            structure_of_3rd_level = page.get_structure_of_3rd_level_in_header()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_in_header()
            structure_of_4th_level = page.get_structure_of_4th_level_in_header()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_in_header()
            structure_of_5th_level = page.get_structure_of_5th_level_in_header()
            visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_in_header()
            structure_of_6th_level = page.get_structure_of_6th_level_in_header()
            invisibility_of_elements_on_6th_level = page.check_elements_invisibility_on_6th_level_in_header()
            assert structure_of_header, "The Header is empty"
            assert visibility_of_elements_on_the_1st_level, "1th-level elements are invisible on the page"
            assert structure_of_2nd_level, "Elements on the 2nd level in the Header are absent"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible on the page"
            assert structure_of_3rd_level, "Elements on the 3rd level in the Header are absent"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"
            assert structure_of_4th_level, "Elements on the 4th level in the Header are absent"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible on the page"
            assert structure_of_5th_level, "Elements on the 5th level in the Header are absent"
            assert visibility_of_elements_on_5th_level, "5th-level elements are invisible on the page"
            assert structure_of_6th_level, "Elements on the 6th level in the Header are absent"
            assert invisibility_of_elements_on_6th_level, "6th-level elements are visible on the page"
