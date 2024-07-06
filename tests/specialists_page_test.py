"""Auto tests for verifying web elements on the 'Specialists' page"""
import allure
from pages.specialists_page import SpecialistsPage
from test_data.specialists_page_data import SpecialistsPageData
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData


@allure.epic("Test Specialists Page")
class TestSpecialistsPage:
    class TestSpecialistsPageStructure:

        @allure.title("Verify presence and visibility of content on the page")
        def test_sp_01_01_verify_page_presence_and_visibility(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-6th levels of nesting on the page""")
        def test_sp_01_02_verify_page_structure_and_visibility(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
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
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible on the page"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible on the page"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible on the page"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"
            assert structure_of_6th_level, "Elements on the 6th level are absent on the page"
            assert visibility_of_elements_on_6th_level, "6th-level elements are invisible on the page"

        @allure.title("""Verify presence, visibility of the title, text, link, grid, cards and images  
        on the 2nd, 3rd, 5th, 6th levels of nesting on the page""")
        def test_sp_01_03_verify_page_structural_elements(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            title_on_2nd_level = page.check_title_h2_presence()
            title_visibility = page.check_title_h2_visibility()
            text_on_2nd_level = page.check_text_presence()
            text_visibility = page.check_text_visibility()
            grid_on_2nd_level = page.check_grid_presence()
            grid_visibility = page.check_grid_visibility()
            link_on_3rd_level = page.check_all_specialists_link_presence()
            link_visibility = page.check_all_specialists_link_visibility()
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
            assert text_on_2nd_level, "The text on the 2nd level is absent in DOM"
            assert text_visibility, "The text on the 2nd level is invisible"
            assert grid_on_2nd_level, "The grid on the 2nd level is absent on the page"
            assert grid_visibility, "The grid on the 2nd level is invisible"
            assert link_on_3rd_level, "The 'All Specialists' link on 3rd level is absent on the page"
            assert link_visibility, "The 'All Specialists' link is invisible"
            assert cards_on_3rd_level == SpecialistsPageData.specialists_grid_size, \
                "The grid size does not match the expected value"
            assert cards_visibility, "Specialist cards on 3rd level are invisible in the grid"
            assert images_on_5th_level, "Images on the 5th level are absent on the page"
            assert images_visibility, "Images on the 5th level are invisible"
            assert names_on_5th_level, "Names in specialist cards on the 5th level are absent on the page"
            assert names_visibility, "Names in specialist cards on the 5th level are invisible"
            assert professions_on_6th_level, "Professions in specialist cards on 6th level are absent on the page"
            assert professions_visibility, "Professions in specialist cards on 6th level are invisible"

    class TestSpecialistPageText:
        @allure.title("Verify value of the title of the tab")
        def test_sp_02_01_verify_tab_title(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in SpecialistsPageData.tab_title, \
                "The title value of the tab doesn't match the valid value"

        @allure.title("Verify value of title with tag 'h2' on the page")
        def test_sp_02_02_verify_page_title(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            title_value = page.get_value_of_title_h2()
            assert title_value, "The title value on the page is empty"
            assert title_value in SpecialistsPageData.title_h2, \
                "The title on the page doesn't match the valid value"

        @allure.title("Verify value of text on the page")
        def test_sp_02_03_verify_page_text(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            text_content = page.get_text_content_on_page()
            assert text_content, "The text content on the page is empty"
            assert text_content in SpecialistsPageData.text_on_page, \
                "The text content does not match the valid value"

        @allure.title("Verify values of names and professions in specialist cards in the grid")
        def test_sp_02_04_verify_name_and_profession_in_cards(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            name_values = page.get_name_values_in_cards()
            profession_values = page.get_profession_values_in_cards()
            assert name_values, "Name values in cards are empty"
            assert name_values in SpecialistsPageData.specialists_names, \
                "The names in specialist cards do not match the valid values"
            assert profession_values, "Profession values in cards are empty"
            assert profession_values in SpecialistsPageData.specialists_professions, \
                "The professions in specialist cards do not match the valid values"

        @allure.title("Verify text in the 'All Specialists' link")
        def test_sp_02_05_verify_text_in_link(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            link_text = page.get_text_in_all_specialists_link()
            assert link_text, "Text in the 'All Specialists' link is empty"
            assert link_text in SpecialistsPageData.all_specialists_link_text, \
                f"Text in the 'All Specialists' link does not match any valid values"

    class TestSpecialistPageLinks:
        @allure.title("Verify clickability, href, status code of the 'All Specialists' link")
        def test_sp_03_01_verify_all_specialists_link(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            link_clickability = page.check_all_specialists_link_clickability()
            link_href = page.get_all_specialists_link_href()
            link_status_code = page.get_all_specialists_link_status_code()
            assert link_clickability, f"The 'All Specialists' link is unclickable"
            assert link_href, "Link href is empty"
            assert link_href == SpecialistsPageData.all_specialists_link_href, \
                f"The attribute 'href' of the link does not match the valid value"
            assert link_status_code == SpecialistsPageData.all_specialists_link_status_code, \
                f"The status code of the link does not match the valid value"

        @allure.title("""Verify that the 'All Specialists' link leads an unauthorized user 
                         to the correct page after clicking""")
        def test_sp_03_02_verify_all_specialists_link_leads_unauthorized_user_to_the_correct_page(
                self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            new_tab_url = page.click_all_specialists_link()
            text_on_new_tab = page.get_element_text_on_new_tab()
            assert new_tab_url == StartUnauthorizedPageData.page_url, \
                "The 'All Specialists' link leads to an incorrect page after clicking"
            assert text_on_new_tab in StartUnauthorizedPageData.text_on_page["text_in_section1"], \
                "The opened page does not load correctly after clicking on the 'All Specialists' link"

        @allure.title("""Verify that the 'All Specialists' link leads an authorized user 
                         to the correct page after clicking""")
        def test_sp_03_03_verify_all_specialists_link_leads_authorized_user_to_the_correct_page(
                self, driver, auto_test_user_authorized):
            page = SpecialistsPage(driver)
            page.open_specialists_page()
            new_tab_url = page.click_all_specialists_link()
            text_on_new_tab = page.get_value_of_title_h2()
            assert new_tab_url == SpecialistsPageData.page_url, \
                "The 'All Specialists' link leads to an incorrect page after clicking"
            assert text_on_new_tab in SpecialistsPageData.title_h2, \
                "The opened page does not load correctly after clicking on the 'All Specialists' link"

    class TestSpecialistCardImages:

        @allure.title("Verify attribute values and sizes of images in specialist cards in the grid")
        def test_sp_04_02_verify_images_attributes_and_changed_sizes_in_cards(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            images_src = page.get_images_src_in_specialist_cards()
            images_alt = page.get_images_alt_in_specialist_cards()
            images_size_changes = page.check_size_changes_of_card_images()
            assert images_src, "The 'src' attribute value of some card images is empty"
            assert images_src == SpecialistsPageData.specialists_images_src, \
                "The 'src' attribute values of the card images are unaccurate"
            assert images_alt, "The 'alt' attribute value of some card images is empty"
            for item in images_alt:
                assert item == SpecialistsPageData.specialists_images_alt, \
                    f"The attribute 'alt' '{item}' in the list does not match expected value"
            assert images_size_changes, "Checks of changes in image sizes have not carried out"

        @allure.title("Verify presence, visibility and accuracy of the 1th card's image in the grid")
        def test_sp_04_03_verify_1th_card_image(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            # print(driver.current_url)
            image_presence = page.check_the_1th_card_image_presence()
            image_visibility = page.check_the_1th_card_image_visibility()
            image_src = page.get_the_1th_card_image_src()
            image_alt = page.get_the_1th_card_image_alt()
            image_size = page.get_visible_size_of_the_1th_card_image()
            # print(f"The visible sizes of the 1th card image are: {image_size}")
            driver.set_window_size(820, 1180)
            image_size_new = page.get_visible_size_of_the_1th_card_image()
            # print(f"The new visible sizes of the 1th card image are: {image_size_new}")
            assert image_presence is not None, "The image in the 1th card is absent"
            assert image_visibility, "The 1th card image is invisible"
            assert image_src, "The 'src' attribute value of the 1th card image is empty"
            assert image_src == SpecialistsPageData.specialists_page_images_src["1th_card_img_src"], \
                "The 'src' attribute value of the 1th card image is unaccurate"
            assert image_alt, "The 'alt' attribute value of the 1th card image is empty"
            assert image_alt == SpecialistsPageData.specialists_images_alt, "The 1th card image is unaccurate"


