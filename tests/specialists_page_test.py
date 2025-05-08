"""Auto tests for verifying web elements on the 'Specialists' page"""
import allure
from pages.specialists_page import SpecialistsPage as sPage
from test_data.specialists_page_data import SpecialistsPageData as sPD
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData as suPD


# @pytest.mark.skip(reason="unsupported preconditions")
@allure.epic("Test Specialists Page")
class TestSpecialistsPage:
    class TestSpecialistsPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_sp_01_01_verify_page_presence_and_visibility(self, driver, specialists_page_open):
            page = sPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-6th levels of nesting on the page""")
        def test_sp_01_02_verify_page_structure_and_visibility(self, driver, specialists_page_open):
            page = sPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_on_page()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
            structure_of_5th_level = page.get_structure_of_5th_level()
            structure_of_6th_level = page.get_structure_of_6th_level()
            visibility_of_elements_on_6th_level = page.check_elements_visibility_on_6th_level_on_page()
            assert structure_of_1st_level, "The page is empty"
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"
            assert structure_of_6th_level, "Elements on the 6th level are absent on the page"
            assert visibility_of_elements_on_6th_level, "6th-level elements are invisible"

        @allure.title("""Verify presence, visibility of the title, text, link, grid, cards and images  
        on the 2nd, 3rd, 5th, 6th levels of nesting on the page""")
        def test_sp_01_03_verify_page_structural_elements(self, driver, specialists_page_open):
            page = sPage(driver)
            title_on_2nd_level = page.check_title_presence()
            title_visibility = page.check_title_visibility()
            text_on_2nd_level = page.check_text_presence()
            text_visibility = page.check_text_visibility()
            grid_on_2nd_level = page.check_grid_presence()
            grid_visibility = page.check_grid_visibility()
            link_on_3rd_level = page.check_all_spec_link_presence()
            link_visibility = page.check_all_spec_link_visibility()
            cards_on_3rd_level = page.get_list_of_cards()
            cards_visibility = page.check_cards_visibility()
            images_on_5th_level = page.get_list_of_card_images()
            images_visibility = page.check_image_visibility_in_cards()
            names_on_5th_level = page.get_list_of_names_in_cards()
            names_visibility = page.check_visibility_of_names_in_cards()
            professions_on_6th_level = page.get_list_of_professions_in_cards()
            professions_visibility = page.check_visibility_of_professions_in_cards()
            assert title_on_2nd_level, "The title on the 2nd level is absent on the page"
            assert title_visibility, "The title on the 2nd level is invisible"
            assert text_on_2nd_level, "The text on the 2nd level is absent on the page"
            assert text_visibility, "The text on the 2nd level is invisible"
            assert grid_on_2nd_level, "The grid on the 2nd level is absent on the page"
            assert grid_visibility, "The grid on the 2nd level is invisible"
            assert link_on_3rd_level, "The 'All Specialists' link on the 3rd level is absent on the page"
            assert link_visibility, "The 'All Specialists' link is invisible"
            assert cards_on_3rd_level, "Cards on the 3rd level are absent on the page"
            assert cards_visibility, "Cards on the 3rd level are invisible"
            assert images_on_5th_level, "Images on the 5th level are absent on the page"
            assert images_visibility, "Images on the 5th level are invisible"
            assert names_on_5th_level, "Names in specialist cards on the 5th level are absent on the page"
            assert names_visibility, "Names in specialist cards on the 5th level are invisible"
            assert professions_on_6th_level, "Professions in specialist cards on the 6th level are absent on the page"
            assert professions_visibility, "Professions in specialist cards on the 6th level are invisible"

    class TestSpecialistPageText:
        @allure.title("Verify value of the title of the tab")
        def test_sp_02_01_verify_tab_title(self, driver, specialists_page_open):
            page = sPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in sPD.tab_title, "The title value of the tab mismatches the valid value"

        @allure.title("Verify value of title with tag 'h2' on the page")
        def test_sp_02_02_verify_page_title(self, driver, specialists_page_open):
            page = sPage(driver)
            title_value = page.get_value_of_page_title()
            assert title_value, "The title value on the page is empty"
            assert title_value in sPD.page_title, "The title on the page mismatches the valid value"

        @allure.title("Verify value of text on the page")
        def test_sp_02_03_verify_page_text(self, driver, specialists_page_open):
            page = sPage(driver)
            text_content = page.get_text_content_on_page()
            assert text_content, "Text content on the page is empty"
            assert text_content in sPD.text_on_page, "Text content mismatches the valid value"

        @allure.title("Verify values of names and professions in specialist cards in the grid")
        def test_sp_02_04_verify_name_and_profession_in_cards(self, driver, specialists_page_open):
            page = sPage(driver)
            name_values = page.get_name_values_in_cards()
            profession_values = page.get_profession_values_in_cards()
            assert name_values, "Name values in cards are empty"
            assert all(element in sPD.spec_names for element in name_values), "Names in cards mismatch valid values"
            assert profession_values, "Profession values in cards are empty"
            assert all(element in sPD.spec_professions for element in profession_values), \
                "Professions in cards mismatch valid values"

        @allure.title("Verify text in the 'All Specialists' link")
        def test_sp_02_05_verify_text_in_link(self, driver, specialists_page_open):
            page = sPage(driver)
            link_text = page.get_text_in_all_spec_link()
            assert link_text, "Text in the 'All Specialists' link is empty"
            assert link_text in sPD.all_spec_link_text, "Text in the 'All Specialists' link mismatches any valid values"

    class TestSpecialistPageLinks:
        @allure.title("Verify clickability, href, status code of the 'All Specialists' link")
        def test_sp_03_01_verify_all_spec_link(self, driver, specialists_page_open):
            page = sPage(driver)
            link_clickability = page.check_all_spec_link_clickability()
            link_href = page.get_all_spec_link_href()
            link_status_code = page.get_all_spec_link_status_code()
            assert link_clickability, "The 'All Specialists' link is unclickable"
            assert link_href, "Link href is empty"
            assert link_href in sPD.all_spec_link_href, "The attribute 'href' of the link mismatches the valid value"
            assert link_status_code in sPD.all_spec_link_status_code, "The link status code mismatches the valid value"

        @allure.title("""Verify that the 'All Specialists' link leads an unauthorized user 
                         to the correct page after clicking""")
        def test_sp_03_02_verify_all_spec_link_navigation_for_unauthorized_user(self, driver, specialists_page_open):
            page = sPage(driver)
            new_tab_url = page.click_all_spec_link()
            text_on_new_tab = page.get_element_text_on_new_tab()
            assert new_tab_url == suPD.page_url, "The link leads to an incorrect page after clicking"
            assert text_on_new_tab in suPD.text_on_page["text_in_section1"], \
                "The opened page does not load correctly after clicking on the link"

        @allure.title("""Verify that the 'All Specialists' link leads an authorized user 
                         to the correct page after clicking""")
        def test_sp_03_03_verify_all_spec_link_navigation_for_authorized_user(self, driver, auto_test_user_authorized):
            page = sPage(driver)
            page.open_specialists_page()
            new_tab_url = page.click_all_spec_link()
            text_on_new_tab = page.get_value_of_page_title()
            assert new_tab_url == sPD.page_url, "The link leads to an invalid page after clicking"
            assert text_on_new_tab in sPD.page_title, "The opened page does not load correctly after clicking the link"

    class TestSpecialistCardImages:
        @allure.title("Verify attributes of images in specialist cards in the grid")
        def test_sp_04_01_verify_images_attributes_in_cards(self, driver, specialists_page_open):
            page = sPage(driver)
            images_src = page.get_images_src()
            images_alt = page.get_images_alt()
            assert images_src, "The 'src' attribute value of some card images is empty"
            assert all(element in sPD.images_src for element in images_src), \
                "The 'src' attribute of the card images mismatches valid values"
            assert images_alt, "The 'alt' attribute value of some card images is empty"
            assert all(element == sPD.images_alt for element in images_alt), \
                "The 'alt' attribute value of some card images is empty or mismatches valid values"

        @allure.title("Verify sizes of images in specialist cards in the grid")
        def test_sp_04_02_verify_images_sizes_in_cards(self, driver, specialists_page_open):
            page = sPage(driver)
            images_size = page.get_images_sizes()
            images_size_changed = page.check_size_changes_of_images()
            assert images_size != 0, "Images in specialist cards have not sizes"
            assert images_size_changed, "Checks of changes of image sizes have not carried out"
