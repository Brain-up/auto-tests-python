"""Auto tests for verifying web elements in the Footer on pages"""
import allure
from pages.footer_page import FooterPage
from test_data.links import SpecificExercisesUrls
from test_data.footer_data import FooterData


@allure.epic("Test Footer")
class TestFooter:
    class TestFooterStructure:
        @allure.title("Verify presence and visibility of the Footer")
        def test_fp_01_01_verify_footer_presence_and_visibility(self, driver, main_page_open):
            page = FooterPage(driver)
            footer_presence = page.check_footer_presence()
            footer_visibility = page.check_footer_visibility()
            assert footer_presence is not None, "The Footer is absent in DOM"
            assert footer_visibility, "The Footer is invisible"

        @allure.title("Verify composition and visibility of elements on the 1st-7th levels of nesting in the Footer")
        def test_fp_01_02_verify_footer_structure_and_visibility(self, driver, main_page_open):
            page = FooterPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_on_page()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
            structure_of_5th_level = page.get_structure_of_5th_level()
            visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_on_page()
            structure_of_6th_level = page.get_structure_of_6th_level()
            visibility_of_elements_on_6th_level = page.check_elements_visibility_on_6th_level_on_page()
            structure_of_7th_level = page.get_structure_of_7th_level()
            visibility_of_elements_on_7th_level = page.check_elements_visibility_on_7th_level_on_page()
            assert structure_of_1st_level, "The Footer is empty"
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"
            assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"
            assert structure_of_6th_level, "Elements on the 6th level are absent on the page"
            assert visibility_of_elements_on_6th_level, "6th-level elements are invisible"
            assert structure_of_7th_level, "Elements on the 7th level are absent on the page"
            assert visibility_of_elements_on_7th_level, "7th-level elements are invisible"

        @allure.title("Verify presence, visibility of text, links, images in the Footer")
        def test_fp_01_03_verify_footer_structural_elements(self, driver, main_page_open):
            page = FooterPage(driver)
            text_on_4th_level = page.check_text_presence()
            text_visibility = page.check_text_visibility()
            links_on_3rd_and_6th_levels = page.get_list_of_links()
            links_visibility = page.check_links_visibility()
            images_on_7th_level = page.get_list_of_images()
            images_visibility = page.check_images_visibility()
            assert text_on_4th_level, "The text on the 4th level is absent in the Footer"
            assert text_visibility, "The text on the 4th level is invisible"
            assert links_on_3rd_and_6th_levels, "Links on the 3rd and 6th levels are absent in the Footer"
            assert links_visibility, "Links on the 3rd and 6th levels are invisible"
            assert images_on_7th_level, "Images on the 7th level are absent in the Footer"
            assert images_visibility, "Images on the 7th level are invisible"

    class TestFooterText:
        @allure.title("Verify content of text in the Footer")
        def test_fp_02_01_verify_footer_text(self, driver, main_page_open):
            page = FooterPage(driver)
            text_content = page.get_footer_text()
            assert text_content, "The text content in the Footer is empty"
            assert text_content in FooterData.with_the_support_text, "Text in the Footer mismatches the valid value"

        @allure.title("Verify text in the 'Contact us' link in the Footer")
        def test_fp_02_02_verify_text_in_links(self, driver, main_page_open):
            page = FooterPage(driver)
            link_text = page.get_text_in_contact_us_link()
            assert link_text, "Text in the link is empty"
            assert link_text in FooterData.contact_us_link_text, "Text in the link mismatches the valid value"

    class TestFooterLinks:
        @allure.title("Verify clickability, href, prefix and subject, status code of links in the Footer")
        def test_fp_03_01_verify_footer_links(self, driver, main_page_open):
            page = FooterPage(driver)
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            link_prefix_and_subject = page.check_contact_us_link_href()
            link_status_codes = page.get_supporter_links_status_codes()
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"
            assert all(link_href in FooterData.links_href for link_href in links_href), \
                "Attributes 'href' of links mismatch valid values"
            assert link_prefix_and_subject, \
                "The attribute 'href' of the 'Contact us' link does not contain the proper prefix and/or subject"
            assert all(status_code in FooterData.link_status_codes for status_code in link_status_codes), \
                "Status codes of links mismatch valid values"

        @allure.title("Verify that links in the Footer lead to correct pages after clicking")
        def test_fp_03_02_verify_links_lead_to_the_correct_pages(self, driver, main_page_open):
            page = FooterPage(driver)
            new_tabs_urls = page.click_on_links()
            assert all(tab_url in FooterData.pages_urls for tab_url in new_tabs_urls), \
                "Links in the Footer lead to incorrect pages after clicking or did not loaded during the allotted time"

        @allure.title("Verify that the 'Contact us' link in the Footer calls an email client")
        def test_fp_03_03_verify_contact_us_link_calls_an_email_client(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_contact_us_link()
            assert True, "The 'Contact us' link in the Footer does not call an email client"

    class TestFooterImages:
        @allure.title("Verify attributes of images in links in the Footer")
        def test_fp_04_01_verify_images_attributes_in_links(self, driver, main_page_open):
            page = FooterPage(driver)
            images_src = page.get_images_src()
            images_alt = page.get_images_alt()
            assert images_src, "The 'src' attribute value of images is empty"
            assert all(image_src in FooterData.images_src for image_src in images_src), \
                "The 'src' attribute of some images mismatches valid values"
            assert images_alt, "The 'alt' attribute value of some images is empty"
            assert all(image_alt in FooterData.images_alt for image_alt in images_alt), \
                "The 'alt' attribute value of some images is empty or mismatches valid values"

        @allure.title("Verify sizes of images in links in the Footer")
        def test_fp_04_02_verify_images_sizes_in_links(self, driver, main_page_open):
            page = FooterPage(driver)
            images_size = page.get_images_sizes()
            images_size_changed = page.check_size_changes_of_images()
            assert images_size != 0, "Images in links have not sizes"
            assert len(images_size_changed) == len(FooterData.images_src), "Not all images in links have changed sizes"

    # @pytest.mark.skip(reason="unsupported preconditions")
    class TestFooterAuthorized:

        @allure.title("Verify Footer invisibility through the modal window with the exercise")
        def test_fp_05_01_verify_footer_invisibility_through_modal_window(self, driver, auto_test_user_authorized):
            modal_window_page = FooterPage(driver, SpecificExercisesUrls.URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE)
            modal_window_page.open()
            assert (modal_window_page.check_footer_presence() and modal_window_page.check_jetbrains_image_presence()), \
                "Footer (including the Jetbrains image) is absent in the DOM tree"
            assert (modal_window_page.check_footer_invisibility()
                    and modal_window_page.check_jetbrains_image_invisibility()), \
                "Footer (including the Jetbrains image) is visible through the modal window"
