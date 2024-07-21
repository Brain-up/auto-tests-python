"""Auto tests for verifying web elements on the 'Contributors' page"""
import allure
from pages.contributors_page import ContributorsPage
from test_data.contributors_page_data import ContributorsPageData


@allure.epic("The Contributors Page")
class TestContributorsPage:
    class TestContributorsPageStructure:

        @allure.title("Verify presence, visibility and structure of content on the page")
        def test_cnp_01_01_verify_page_presence_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("""Verify the composition and visibility of elements 
        on the 1st-5th levels of nesting on the page""")
        def test_cnp_01_02_verify_page_structure_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
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
            page = ContributorsPage(driver)
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
            page = ContributorsPage(driver)
            tab_title_value = page.get_value_of_tab_title()
            assert tab_title_value, "The title value of the tab is empty"
            assert tab_title_value in ContributorsPageData.tab_title, \
                "The title value of the tab doesn't match the valid value"

        @allure.title("Verify values of title and subtitles with tags hw, h3 on the page")
        def test_cnp_02_02_verify_page_title_and_subtitles(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            title_value = page.get_value_of_title()
            subtitle_values = page.get_values_of_subtitles()
            assert title_value, "The title value on the page is empty"
            assert title_value in ContributorsPageData.page_title, "The title on the page doesn't match the valid value"
            assert subtitle_values, "Subtitle values on the page are empty"
            assert all(subtitle_value in ContributorsPageData.page_subtitles for subtitle_value in subtitle_values), \
                "Subtitles do not match any valid values"

        @allure.title("Verify content of the text on the page")
        def test_cnp_02_03_verify_page_text(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            text_content = page.get_text_content_on_page()
            assert text_content in ContributorsPageData.text_on_page, "TThe text content does not match the valid value"

        @allure.title("Verify values of the text in card descriptions")
        def test_cnp_02_04_verify_text_of_card_descriptions(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            description_values = page.check_values_of_card_descriptions()
            assert description_values == ContributorsPageData.description_count, \
                "The text in descriptions is absent or do not match the valid count"

        @allure.title("Verify text in links in card links")
        def test_cnp_02_05_verify_text_in_card_links(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            links_text = page.check_text_in_card_links()
            assert links_text == ContributorsPageData.link_count, \
                "Text in card links is absent or do not match the valid count"

    class TestContributorsPageLinks:

        @allure.title("Verify presence, visibility, clickability, href of links in the section")
        def test_cnp_03_01_verify_links_in_section(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"

        @allure.title("Verify href, status code, text of the 'All Team' link on the page")
        def test_cnp_03_02_verify_all_team_link(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            link_href = page.get_all_team_link_href()
            link_status_code = page.get_all_team_link_status_code()
            actual_link_text = page.get_text_in_all_team_link()
            assert link_href == ContributorsPageData.all_team_link_href, \
                f"The attribute 'href' of the {link_href} link does not match the valid value"
            assert link_status_code == ContributorsPageData.all_team_link_status_code, \
                f"The {link_href} link status code does not match the valid value"
            assert actual_link_text in ContributorsPageData.all_team_link_text, \
                f"The actual text '{actual_link_text}' of the {link_href} link does not match any of the valid option"

    class TestContributorCardImages:
        @allure.title("Verify attribute values and sizes of images in contributors cards in the grid")
        def test_cnp_04_02_verify_image_attributes_in_cards(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            images_src = page.check_images_src_in_contributor_cards()
            images_alt = page.get_images_alt_in_contributor_cards()
            images_size_changes = page.check_size_changes_of_card_images()
            assert images_src, "The 'src' attribute value of some card images is empty or unaccurate"
            assert images_alt, "The 'alt' attribute value of some card images is empty"
            assert all(image_alt == ContributorsPageData.images_alt for image_alt in images_alt), \
                "The 'alt' attribute value of some card images is empty or unaccurate"
            assert images_size_changes, "Checks of changes in image sizes have not carried out"
