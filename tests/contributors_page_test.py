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
            print(driver.current_url)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            structure_of_page = page.get_structure_of_page()
            visibility_of_elements_on_the_1st_level = page.check_visibility_of_elements_on_page()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"
            assert structure_of_page, "The page is empty"
            assert visibility_of_elements_on_the_1st_level, "1th-level elements are invisible on the page"

        @allure.title("Verify amount and visibility of sections with content on the page")
        def test_cnp_01_02_verify_sections_structure_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            sections_amount = page.get_amount_of_sections_on_page()
            sections_visibility = page.check_visibility_of_sections()
            assert sections_amount == ContributorsPageData.amount_of_sections_on_page, \
                "The amount of sections with content does not match the expected value"
            assert sections_visibility, "Sections with content are invisible on the page"

        @allure.title("Verify the composition and visibility of elements "
                      "on the 1st, 2nd, 3rd, 4th levels of nesting in the section")
        def test_cnp_01_03_verify_section_structure_and_visibility(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            structure_of_section = page.get_structure_of_section()
            visibility_of_subsections_on_the_1st_level = page.check_visibility_of_elements_in_section()
            structure_of_1st_level_subsection = page.get_structure_of_1st_level_in_section()
            visibility_of_subsections_on_1st_level = page.check_visibility_of_elements_in_subsections()
            structure_of_2nd_level_subsections = page.get_structure_of_2nd_level_in_section()
            visibility_of_elements_on_2nd_level = page.check_visibility_of_elements_on_2nd_level_in_section()
            structure_of_3rd_level_subsections = page.get_structure_of_3rd_level_in_section()
            visibility_of_elements_on_3rd_level = page.check_visibility_of_elements_on_3rd_level_in_section()
            structure_of_4th_level_subsections = page.get_structure_of_4th_level_in_section()
            assert structure_of_section, "The section is empty"
            assert visibility_of_subsections_on_the_1st_level, "1th-level subsections are invisible on the page"
            assert structure_of_1st_level_subsection, "Subsections on the 1st level in the section are empty"
            assert visibility_of_subsections_on_1st_level, "1st-level subsections are invisible on the page"
            assert structure_of_2nd_level_subsections, "Elements on the 2nd level in the section are empty"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible on the page"
            assert structure_of_3rd_level_subsections, "Elements on the 3rd level in the section are empty"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible on the page"
            assert structure_of_4th_level_subsections, "Elements on the 4th level in the section are empty"

        @allure.title("Verify amount of contributor cards with images, links and descriptions in the section grid")
        def test_cnp_01_04_verify_structure_of_grid_in_section(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            amount_of_cards = page.get_amount_of_cards_in_the_grid()
            amount_of_images = page.get_amount_of_images_in_the_grid()
            amount_of_links = page.get_amount_of_links_in_the_grid()
            amount_of_descriptions = page.get_amount_of_descriptions_in_the_grid()
            assert amount_of_cards == ContributorsPageData.amount_of_grid_cards, \
                "The amount of contributor cards in the grid does not match the expected value"
            assert amount_of_images == ContributorsPageData.amount_of_grid_images, \
                "The amount of images in the grid does not match the expected value"
            assert amount_of_links == ContributorsPageData.amount_of_grid_links, \
                "The amount of links in the grid does not match the expected value"
            assert amount_of_descriptions == ContributorsPageData.amount_of_grid_descriptions, \
                "The amount of descriptions in the grid does not match the expected value"

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
            assert description_values == ContributorsPageData.amount_of_grid_descriptions, \
                "The text in descriptions is absent or do not match the valid count"

        @allure.title("Verify text in links in card links")
        def test_cnp_02_05_verify_text_in_card_links(self, driver, contributors_page_open):
            page = ContributorsPage(driver)
            links_text = page.check_text_in_card_links()
            assert links_text == ContributorsPageData.amount_of_grid_links, \
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
