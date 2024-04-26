"""Auto tests for verifying web elements on the starting page for unauthorized users"""
import allure
import requests
from pages.start_unauthorized_page import StartUnauthorizedPage
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData
from test_data.login_page_data import LoginPageData


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
            structure_of_3rd_level_subsections = page.get_structure_of_3rd_level_in_section_2()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section_2()
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

        @allure.title("Verify values of subtitles with tag 'h4' on the page")
        def test_su_02_02_verify_subtitles_on_the_page(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            subtitle_values = page.get_values_of_subtitles()
            assert subtitle_values, "Subtitle values on ghe page are empty"
            assert subtitle_values in StartUnauthorizedPageData.subtitles_on_start_unauthorized_page, \
                "The subtitles on start unauthorized page do not match the valid values"

        @allure.title("Verify values of the text in the section 1 on the page")
        def test_su_02_03_verify_text_in_section_1(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            text_value_in_section_1 = page.get_values_of_text_in_section_1()
            assert (text_value_in_section_1 in
                    StartUnauthorizedPageData.text_on_start_unauthorized_page["text_in_section_1"]), \
                "The text in section 1 does not match the any of the valid option"

        @allure.title("Verify values of the text in the section 2 on the page")
        def test_su_02_04_verify_text_in_section_2(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            text_value_in_section_2 = page.get_values_of_text_in_section_2()
            assert (text_value_in_section_2 ==
                    StartUnauthorizedPageData.text_on_start_unauthorized_page["text_in_section_2"]), \
                "The text in section 2 does not match the valid options"

    class TestStartUnauthorizedPageImage:

        @allure.title("Verify attribute values and size of the image in the section 1 on the page")
        def test_su_03_01_verify_image_attributs_and_changed_sizes_in_section_1(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            image_src = page.get_image_src_in_section_1()
            image_alt = page.get_image_alt_in_section_1()
            image_size = page.get_visible_size_of_image_in_section_1()
            image_size_changes = page.check_size_changes_of_image_in_section_1()
            assert image_src, "The 'src' attribute value of the image is empty"
            assert StartUnauthorizedPageData.image_src_in_section_1 in image_src, \
                "The 'src' attribute value of the image in the section 1 does not match the valid value"
            assert image_alt, "The 'alt' attribute value of the image is empty"
            assert image_alt == StartUnauthorizedPageData.image_alt_in_section_1, \
                "The 'alt' attribute value of the image in the section 1 does not match the valid value"
            assert image_size != 0, f"The image in the section 1 is invisible due its size = 0, 0"
            assert image_size_changes, "Checks of changes in image sizes have not carried out"

    class TestStartUnauthorizedPageLinks:

        @allure.title("""Verify presence, visibility, clickability, href, status code, text 
                         of the 'Login' link in the section 1 on the page""")
        def test_su_04_01_verify_login_link(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            link_presence = page.check_login_link_presence()
            link_visibility = page.check_login_link_visibility()
            link_clickability = page.check_login_link_clickability()
            link_href = page.get_login_link_href()
            link_status_code = requests.head(link_href).status_code
            actual_link_text = page.get_text_in_login_link()
            assert link_presence is not None, "The 'Login' link is absent in DOM"
            assert link_visibility, "The 'Login' link is invisible on the page"
            assert link_clickability, "The 'Login' link is unclickable"
            assert link_href == StartUnauthorizedPageData.login_link_href, \
                f"The attribute 'href' of the {link_href} link does not match the valid value"
            assert link_status_code == StartUnauthorizedPageData.login_link_status_code, \
                f"The {link_href} link status code does not match the valid value"
            assert actual_link_text in StartUnauthorizedPageData.login_link_text, \
                f"The actual text '{actual_link_text}' of the {link_href} link does not match any of the valid option"

        @allure.title("Verify that the 'Login' link leads to the correct page after clicking")
        def test_su_04_02_verify_login_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = StartUnauthorizedPage(driver)
            page.click_login_link()
            text_on_opened_page = page.get_element_text_on_opened_login_page()
            assert text_on_opened_page in LoginPageData.sign_in_tab, \
                "The 'Login' link leads to an incorrect page after clicking or opened page does not load correctly"
