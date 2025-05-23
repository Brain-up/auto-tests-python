"""Auto tests for verifying web elements on the 'Contributors' page"""
import allure
from pages.contributors_page import ContributorsPage as ctbPage
from test_data.contributors_page_data import ContributorsPageData as ctbPD


@allure.epic("The Contributors Page")
class TestContributorsPage:
    class TestContributorsPageStructure:

        @allure.title("Verify presence, visibility and structure of content on the page")
        def test_cnp_01_01_verify_page_presence_and_visibility(self, driver, contributors_page_open):
            page = ctbPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-5th levels of nesting on the page""")
        def test_cnp_01_02_verify_page_structure_and_visibility(self, driver, contributors_page_open):
            page = ctbPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_on_page()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
            structure_of_5th_level = page.get_structure_of_5th_level()
            assert structure_of_1st_level, "The page is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"

        @allure.title("Verify presence, visibility of titles/subtitles, cards, descriptions, links, images on the page")
        def test_cnp_01_03_verify_page_structural_elements(self, driver, contributors_page_open):
            page = ctbPage(driver)
            title_on_2nd_level = page.check_title_presence()
            title_visibility = page.check_title_visibility()
            subtitles_on_2nd_level = page.get_list_of_subtitles()
            subtitles_visibility = page.check_visibility_of_subtitles()
            cards_on_3rd_level = page.get_list_of_cards()
            cards_visibility = page.check_cards_visibility()
            descriptions_on_4th_level = page.get_list_of_card_descriptions()
            descriptions_visibility = page.check_descriptions_visibility()
            links_on_4th_level = page.get_list_of_links()
            links_visibility = page.check_links_visibility()
            images_on_5th_level = page.get_list_of_card_images()
            images_visibility = page.check_image_visibility_in_cards()
            assert title_on_2nd_level, "The title on the 2nd level is absent on the page"
            assert title_visibility, "The title on the 2nd level is invisible"
            assert subtitles_on_2nd_level, "Subtitles on the 2nd level are absent on the page"
            assert subtitles_visibility, "Subtitles on the 2nd level are invisible"
            assert cards_on_3rd_level, "Cards on the 3rd level are absent on the page"
            assert cards_visibility, "Cards on the 3rd level are invisible"
            assert descriptions_on_4th_level, "Descriptions on the 4th level are absent on the page"
            assert descriptions_visibility, "Descriptions on the 4th level are invisible"
            assert links_on_4th_level, "Links on the 4th level are absent on the page"
            assert links_visibility, "Links on the 4th level are invisible"
            assert images_on_5th_level, "Images on the 5th level are absent on the page"
            assert images_visibility, "Images on the 5th level are invisible"

    class TestContributorsPageText:
        @allure.title("Verify value of the title of the tab")
        def test_cnp_02_01_verify_tab_title(self, driver, contributors_page_open):
            page = ctbPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in ctbPD.tab_title, "The title value of the tab mismatches the valid value"

        @allure.title("Verify values of title and subtitles with tags h2, h3 on the page")
        def test_cnp_02_02_verify_page_title_and_subtitles(self, driver, contributors_page_open):
            page = ctbPage(driver)
            title_value = page.get_value_of_title()
            subtitle_values = page.get_values_of_subtitles()
            assert title_value, "The title value on the page is empty"
            assert title_value in ctbPD.page_title, "The title on the page mismatches the valid value"
            assert subtitle_values, "Subtitle values on the page are empty"
            assert all(element in ctbPD.page_subtitles for element in subtitle_values), \
                "Subtitles mismatch any valid values"

        @allure.title("Verify content of the text on the page")
        def test_cnp_02_03_verify_page_text(self, driver, contributors_page_open):
            page = ctbPage(driver)
            text_content = page.get_text_content_on_page()
            assert text_content in ctbPD.text_on_page, "Text content mismatches the valid value"

        @allure.title("Verify values of the text in card descriptions")
        def test_cnp_02_04_verify_text_of_card_descriptions(self, driver, contributors_page_open):
            page = ctbPage(driver)
            description_values = page.check_values_of_card_descriptions()
            assert description_values, "Text in descriptions is absent"

        @allure.title("Verify text in card links and the 'All Team' link")
        def test_cnp_02_05_verify_text_in_card_links(self, driver, contributors_page_open):
            page = ctbPage(driver)
            card_links_text = page.check_text_in_card_links()
            link_text = page.get_text_in_all_team_link()
            assert card_links_text, "Text in card links is absent"
            assert link_text, "Text in the 'All Team' link is absent"
            assert link_text in ctbPD.all_team_link_text, "Text in the 'All Team' link mismatches any valid values"

    class TestContributorsPageLinks:
        @allure.title("Verify clickability, href of links on the page")
        def test_cnp_03_01_verify_links_on_page(self, driver, contributors_page_open):
            page = ctbPage(driver)
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"

        @allure.title("Verify href, status code of the 'All Team' link")
        def test_cnp_03_02_verify_all_team_link(self, driver, contributors_page_open):
            page = ctbPage(driver)
            link_href = page.get_all_team_link_href()
            link_status_code = page.get_all_team_link_status_code()
            assert link_href == ctbPD.all_team_link_href, "The attribute 'href' of the link mismatches the valid value"
            assert link_status_code in ctbPD.all_team_link_status_code, \
                "The status code of the link mismatches the valid value"

    class TestContributorCardImages:
        @allure.title("Verify attribute values of images in contributors cards in grids")
        def test_cnp_04_01_verify_image_attributes_in_cards(self, driver, contributors_page_open):
            page = ctbPage(driver)
            images_src = page.get_images_src()
            images_alt = page.get_images_alt()
            assert images_src, "The 'src' attribute value of some card images is empty"
            assert all(element.startswith(ctbPD.images_src_start) for element in images_src), \
                "The 'src' attribute value of some card images mismatches the valid value"
            assert images_alt, "The 'alt' attribute value of some card images is empty"
            assert all(element in ctbPD.images_alt for element in images_alt), \
                "The 'alt' attribute value of some card images mismatches the valid value"

        @allure.title("Verify sizes of images in contributor cards in grids")
        def test_cnp_04_02_verify_images_sizes_in_cards(self, driver, contributors_page_open):
            page = ctbPage(driver)
            images_size = page.get_images_sizes()
            images_size_changes = page.check_size_changes_of_images()
            assert images_size != 0, "Images in contributor cards have not sizes"
            assert images_size_changes, "Checks of changes in image sizes have not carried out"
