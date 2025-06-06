"""Auto tests for verifying web elements on the starting page for unauthorized users"""
import allure
from pages.start_unauthorized_page import StartUnauthorizedPage as suPage
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData as suPD
from test_data.login_page_data import LoginPageData


@allure.epic("The Start Unauthorized Page")
class TestStartUnauthorizedPage:
    class TestStUnPageStructure:

        @allure.title("Verify presence and visibility of content on the page")
        def test_su_01_01_verify_page_presence_and_visibility(self, driver, main_page_open):
            page = suPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"

        @allure.title("Verify amount and visibility of sections with content on the page")
        def test_su_01_02_verify_sections_structure_and_visibility(self, driver, main_page_open):
            page = suPage(driver)
            sections_amount = page.get_amount_of_sections_on_page()
            sections_visibility = page.check_visibility_of_sections()
            assert sections_amount == suPD.amount_of_sections_with_content_on_page, \
                "The amount of sections with content mismatches the valid value"
            assert sections_visibility, "Sections with content are invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-3rd levels of nesting in the section 1""")
        def test_su_01_03_verify_section1_structure_and_visibility(self, driver, main_page_open):
            page = suPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level_in_section1()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_section1()
            structure_of_2nd_level = page.get_structure_of_2nd_level_in_section1()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_section1()
            structure_of_3rd_level = page.get_structure_of_3rd_level_in_section1()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section1()
            assert structure_of_1st_level, "The section 1 is empty"
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent in the section 1"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent in the section 1"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-3rd levels of nesting in the section 2""")
        def test_su_01_04_verify_section2_structure_and_visibility(self, driver, main_page_open):
            page = suPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level_in_section2()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_section2()
            structure_of_2nd_level = page.get_structure_of_2nd_level_in_section2()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_section2()
            structure_of_3rd_level = page.get_structure_of_3rd_level_in_section2()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section2()
            assert structure_of_1st_level, "The section 2 is empty"
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent in the section 2"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent in the section 2"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"

    class TestStUnPageText:
        @allure.title("Verify value of the title of the tab")
        def test_su_02_01_verify_tab_title(self, driver, main_page_open):
            page = suPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value == suPD.tab_title, "The title value of the tab mismatches the valid value"

        @allure.title("Verify values of titles and subtitles with tags h2, h4 on the page")
        def test_su_02_02_verify_page_titles_and_subtitles(self, driver, main_page_open):
            page = suPage(driver)
            title_values = page.get_values_of_titles()
            subtitle_values = page.get_values_of_subtitles()
            assert title_values, "Title values on the page are empty"
            assert all(element in suPD.page_titles for element in title_values), \
                "Titles on the page mismatch any valid values"
            assert subtitle_values, "Subtitle values on the page are empty"
            assert all(element in suPD.page_subtitles for element in subtitle_values), \
                "Subtitles mismatch any valid values"

        @allure.title("Verify content of the text in sections 1, 2")
        def test_su_02_03_verify_page_text(self, driver, main_page_open):
            page = suPage(driver)
            text_content_section1 = page.get_text_content_in_section1()
            text_content_section2 = page.get_text_content_in_section2()
            assert text_content_section1, "Text content in the section 1 is empty"
            assert text_content_section1 in suPD.text_on_page["text_in_section1"], \
                "Text in the section 1 mismatches any valid values"
            assert text_content_section2, "The text content in the section 2 is empty"
            assert all(element in suPD.text_on_page["text_in_section2"]
                       for element in text_content_section2), "Text in the section 2 mismatches any valid values"

        @allure.title("Verify text in the 'Login' link in the section 1")
        def test_su_02_04_verify_text_in_links(self, driver, main_page_open):
            page = suPage(driver)
            link_text = page.get_text_in_login_link()
            assert link_text, "Text in the link is empty"
            assert link_text in suPD.login_link_text, "Text in the link mismatches the valid value"

    class TestStUnPageLinks:
        @allure.title("""Verify presence, visibility, clickability, href, status code 
                         of the 'Login' link in the section 1""")
        def test_su_03_01_verify_login_link(self, driver, main_page_open):
            page = suPage(driver)
            link_presence = page.check_login_link_presence()
            link_visibility = page.check_login_link_visibility()
            link_clickability = page.check_login_link_clickability()
            link_href = page.get_login_link_href()
            link_status_code = page.get_login_link_status_code()
            assert link_presence, "The 'Login' link is absent on the page"
            assert link_visibility, "The 'Login' link is invisible"
            assert link_clickability, "The 'Login' link is unclickable"
            assert link_href, "Link href is empty"
            assert link_href == suPD.login_link_href, "The attribute 'href' of the link mismatches the valid value"
            assert link_status_code in suPD.login_link_status_code, "The link status code mismatches the valid value"

        @allure.title("Verify that the 'Login' link leads to the correct page after clicking")
        def test_su_03_02_verify_login_link_leads_to_the_correct_page(self, driver, main_page_open):
            page = suPage(driver)
            page.click_login_link()
            text_on_opened_page = page.get_element_text_on_opened_login_page()
            assert text_on_opened_page in LoginPageData.sign_in_tab, \
                "The 'Login' link leads to an incorrect page after clicking or opened page does not load correctly"

    class TestStUnPageImage:
        @allure.title("Verify presence, visibility and attributes of the image in the section 1")
        def test_su_04_01_verify_image_in_section1(self, driver, main_page_open):
            page = suPage(driver)
            image_presence = page.check_image_presence()
            image_visibility = page.check_image_visibility()
            image_src = page.get_src_of_image()
            image_alt = page.get_alt_of_image()
            assert image_presence, "The image is absent in the section 1"
            assert image_visibility, "The image is invisible in the section 1"
            assert image_src, "The 'src' attribute value of the image is empty"
            assert suPD.image_src_in_section1 in image_src, "The image 'src' attribute mismatches the valid value"
            assert image_alt, "The image 'alt' attribute is empty"
            assert image_alt == suPD.image_alt_in_section1, "The image 'alt' attribute mismatches the valid value"

        @allure.title("Verify size of the image in the section 1")
        def test_su_04_02_verify_image_size_in_section1(self, driver, main_page_open):
            page = suPage(driver)
            image_size = page.get_size_of_image()
            image_size_changes = page.check_size_changes_of_image()
            assert image_size != 0, "The image in the section 1 hasn't sizes"
            assert image_size_changes, "Checks of changes of image sizes have not carried out"
