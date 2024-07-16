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
            sections_amount = page.get_amount_of_sections_on_page()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
            subsections_on_2nd_level = page.get_list_of_subsections_on_2nd_level_on_page()
            visibility_of_subsections_on_2nd_level = page.check_visibility_of_subsections_on_2nd_level_on_page()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
            structure_of_5th_level = page.get_structure_of_5th_level()
            assert structure_of_1st_level, "The page is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
            assert sections_amount == ContributorsPageData.amount_of_sections_on_page, \
                "The amount of sections with content does not match the valid value"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert subsections_on_2nd_level, "Subsections on the 2nd level are empty"
            assert visibility_of_subsections_on_2nd_level, "2nd-level subsections are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"

        @allure.title("Verify number of contributor cards with images, links and descriptions in the grid")
        def test_cnp_01_03_verify_structure_of_grid(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            card_count = page.count_cards_in_grid()
            image_count = page.count_images_in_cards()
            link_count = page.count_links_in_cards()
            description_count = page.count_descriptions_in_cards()
            assert card_count == ContributorsPageData.card_count, "The number of cards does not match the valid value"
            assert image_count == ContributorsPageData.image_count, "The number of images doesn't match the valid value"
            assert link_count == ContributorsPageData.link_count, "The number of links does not match the valid value"
            assert description_count == ContributorsPageData.description_count, \
                "The number of descriptions does not match the valid value"

    class TestContributorsPageText:

        @allure.title("Verify value of title with tag 'h2' on the page")
        def test_cnp_02_01_verify_title_on_the_page(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            title_value = page.get_value_of_title_on_the_page()
            assert title_value, "The title value on the page is empty"
            assert title_value in ContributorsPageData.page_title, "The title on the page doesn't match the valid value"

        @allure.title("Verify values of subtitles with tag 'h3' on the page")
        def test_cnp_02_02_verify_subtitles_on_the_page(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            titles_value = page.get_values_of_subtitles()
            assert titles_value, "Subtitle values on the page are empty"
            assert all(title_value in ContributorsPageData.page_subtitles for title_value in titles_value), \
                "The subtitles on the 'Contributors' page do match the valid values"

        @allure.title("Verify values of the text in the slogan on the page")
        def test_cnp_02_03_verify_text_of_slogan(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            slogan = page.get_value_of_slogan()
            assert slogan in ContributorsPageData.slogan_text, \
                "The text of slogan does not match the valid options"

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
            links_presence = page.get_list_of_links_in_section()
            links_visibility = page.check_visibility_of_links_in_section()
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            assert links_presence is not None, "Links are absent in DOM"
            assert links_visibility, "Links are invisible on the page"
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

        @allure.title("Verify presence and visibility of images in contributors cards in the grid")
        def test_cnp_04_01_verify_images_in_cards_are_present_and_visible(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            images_visibility = page.check_image_presence_and_visibility_in_the_grid()
            assert images_visibility, "Images in contributor cards are invisible in the grid"

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
