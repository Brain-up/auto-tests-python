"""Auto tests for verifying web elements on the 'Used Resources' page"""
import allure
import requests
from pages.used_resources_page import UsedResourcesPage
from locators.used_resources_page_locators import UsedResourcesPageLocators
from test_data.used_resources_page_data import UsedResourcesPageData


@allure.epic("Test Used Resources Page")
class TestUsedResourcesPage:
    data = UsedResourcesPageData

    class TestUsedResourcesPageForAuthorizedUser:
        locators = UsedResourcesPageLocators()

        @allure.title("Verify presence, visibility and text accuracy of the title on the page")
        def test_ur_01_01_verify_used_resources_page_title(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page_title_presence = page.check_used_resources_page_title_presence()
            page_title_visibility = page.check_used_resources_page_title_visibility()
            page_title_text = page.get_used_resources_page_title_content()
            assert page_title_presence is not None, "The title is absent in DOM"
            assert page_title_visibility, "The title is invisible on the page"
            assert (page_title_text
                    in UsedResourcesPageData.used_resources_page_elements_content["page_title_content"]), \
                "The title content does not match the any of the valid option"

        @allure.title("Verify presence, visibility and content accuracy of the text on the page")
        def test_ur_01_02_verify_used_resources_page_text(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page_text_presence = page.check_used_resources_page_text_presence()
            page_text_visibility = page.check_used_resources_page_text_visibility()
            page_text_content = page.get_text_content_on_the_used_resources_page()
            assert page_text_presence is not None, "The text is absent in DOM"
            assert page_text_visibility, "The text is invisible on the page"
            assert (page_text_content
                    in UsedResourcesPageData.used_resources_page_elements_content["page_text_content"]), \
                "The text content does not match the any of the valid option"

        @allure.title("Verify presence and visibility of the section with links on the page")
        def test_ur_01_03_verify_links_section_on_used_resources_page(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            links_section_presence = page.check_presence_of_links_section_on_used_resources_page()
            links_section_visibility = page.check_visibility_of_links_section_on_used_resources_page()
            assert links_section_presence is not None, "The section with links is absent in DOM"
            assert links_section_visibility, "The section with links is invisible on the page"

        @allure.title("Verify presence and visibility of the section with the freepik.com link on the page")
        def test_ur_01_04_verify_section_of_freepik_com_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            section_presence = page.check_presence_of_freepik_com_link_section()
            section_visibility = page.check_visibility_of_freepik_com_link_section()
            assert section_presence is not None, "The section with the freepik.com link is absent"
            assert section_visibility, "The section with the freepik.com link is invisible"

        @allure.title("Verify presence, visibility, clickability, href, status code, text of the freepik.com link")
        def test_ur_01_05_verify_freepik_com_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            link_presence = page.check_freepik_com_link_presence()
            link_visibility = page.check_freepik_com_link_visibility()
            link_clickability = page.check_freepik_com_link_clickability()
            link_href = page.get_freepik_com_link_href()
            link_status_code = requests.head(link_href).status_code
            actual_link_text = page.get_text_in_freepik_com_link()
            assert link_presence is not None, f"The {link_href} link is absent"
            assert link_visibility, f"The {link_href} link is invisible"
            assert link_clickability, f"The {link_href} link is unclickable"
            assert link_href == UsedResourcesPageData.used_resources_page_links_href["freepik_com_link_href"], \
                f"The attribute 'href' of the {link_href} link does not match the expected value"
            assert link_status_code == \
                   UsedResourcesPageData.used_resources_page_links_status_codes["freepik_com_link_status_code"], \
                   f"The {link_href} link status code does not match the expected value"
            assert actual_link_text == \
                   UsedResourcesPageData.used_resources_page_elements_content["freepik_com_link_content"], \
                   f"The actual text '{actual_link_text}' of the {link_href} link does not match the valid option" \
                   f"on the page {link_href}"

        @allure.title("Verify that the freepik.com link leads to the correct page after click")
        def test_ur_01_06_verify_freepik_com_link_leads_to_the_correct_page(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page.click_freepik_com_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_freepik_com_tab()
            assert text_on_opened_tab == \
                   UsedResourcesPageData.used_resources_page_related_elements_text["freepik_com_start_page_text"], \
                   "The freepik.com link leads to an incorrect page after click " \
                   "or opened page does not load correctly"

        @allure.title("Verify presence and visibility of the section with the 'Plants' link on the page")
        def test_ur_01_09_verify_section_of_plants_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            section_presence = page.check_presence_of_plants_link_section()
            section_visibility = page.check_visibility_of_plants_link_section()
            assert section_presence is not None, "The section with the 'Plants' link is absent"
            assert section_visibility, "The section with the 'Plants' link is invisible"

        @allure.title("Verify presence, visibility, clickability, href, status code, text of the 'Plants' link")
        def test_ur_01_10_verify_plants_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            link_presence = page.check_plants_link_presence()
            link_visibility = page.check_plants_link_visibility()
            link_clickability = page.check_plants_link_clickability()
            link_href = page.get_plants_link_href()
            link_status_code = requests.head(link_href).status_code
            actual_link_text = page.get_text_in_plants_link()
            assert link_presence is not None, f"The {link_href} link is absent"
            assert link_visibility, f"The {link_href} link is invisible"
            assert link_clickability, f"The {link_href} link is unclickable"
            assert link_href == UsedResourcesPageData.used_resources_page_links_href["plants_link_href"], \
                f"The attribute 'href' of the {link_href} link does not match the expected value"
            assert link_status_code == \
                   UsedResourcesPageData.used_resources_page_links_status_codes["plants_link_status_code"], \
                   f"The {link_href} link status code does not match the expected value"
            assert actual_link_text == \
                   UsedResourcesPageData.used_resources_page_elements_content["plants_link_content"], \
                   f"The actual text '{actual_link_text}' of the {link_href} link does not match the valid option" \
                   f"on the page {link_href}"

        @allure.title("Verify that the 'Plants' link leads to the correct page after click")
        def test_ur_01_11_verify_plants_link_leads_to_the_correct_page(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page.click_plants_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_plants_tab()
            assert text_on_opened_tab == \
                   UsedResourcesPageData.used_resources_page_related_elements_text["plants_page_text"], \
                   "The 'Plants' link leads to an incorrect page after click " \
                   "or opened page does not load correctly"

        @allure.title("Verify presence and visibility of the section with the 'Flora' link on the page")
        def test_ur_01_14_verify_section_of_flora_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            section_presence = page.check_presence_of_flora_link_section()
            section_visibility = page.check_visibility_of_flora_link_section()
            assert section_presence is not None, "The section with the 'Flora' link is absent"
            assert section_visibility, "The section with the 'Flora' link is invisible"

        @allure.title("Verify presence, visibility, clickability, href, status code, text of the 'Flora' link")
        def test_ur_01_15_verify_flora_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            link_presence = page.check_flora_link_presence()
            link_visibility = page.check_flora_link_visibility()
            link_clickability = page.check_flora_link_clickability()
            link_href = page.get_flora_link_href()
            link_status_code = requests.head(link_href).status_code
            actual_link_text = page.get_text_in_flora_link()
            assert link_presence is not None, f"The {link_href} link is absent"
            assert link_visibility, f"The {link_href} link is invisible"
            assert link_clickability, f"The {link_href} link is unclickable"
            assert link_href == UsedResourcesPageData.used_resources_page_links_href["flora_link_href"], \
                   f"The attribute 'href' of the {link_href} link does not match the expected value"
            assert link_status_code == \
                   UsedResourcesPageData.used_resources_page_links_status_codes["flora_link_status_code"], \
                   f"The {link_href} link status code does not match the expected value"
            assert actual_link_text == \
                   UsedResourcesPageData.used_resources_page_elements_content["flora_link_content"], \
                   f"The actual text '{actual_link_text}' of the {link_href} link does not match the valid option" \
                   f"on the page {link_href}"

        @allure.title("Verify that the 'Flora' link leads to the correct page after click")
        def test_ur_01_16_verify_flora_link_leads_to_the_correct_page(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page.click_flora_link()
            page.switch_to_new_window()
            text_on_opened_tab = page.get_element_text_on_opened_flora_tab()
            assert text_on_opened_tab == \
                   UsedResourcesPageData.used_resources_page_related_elements_text["flora_page_text"], \
                   "The 'Flora' link leads to an incorrect page after click " \
                   "or opened page does not load correctly"

        class TestUsedResourcesPageForAuthorizedUserIcons:
            @allure.title("Verify presence, visibility and attributes of icons in the sections")
            def test_ur_02_01_verify_icons_in_sections(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                icons_presence = page.get_list_of_icons()
                icons_visibility = page.check_icons_visibility()
                icons_xmlns = page.get_icons_xmlns_in_sections()
                assert icons_presence, "The icons in the sections are absent"
                assert icons_visibility, "The icons in the sections are invisible"
                assert icons_xmlns, "The 'xmlns' attribute value of the icons in the sections is empty"
                assert all(icon_xmlns == UsedResourcesPageData.icons_xmlns for icon_xmlns in icons_xmlns), \
                    "The 'xmlns' attribute value of some icons is empty or non-accurate"

            @allure.title("Verify sizes of icons in the sections")
            def test_ur_02_02_verify_icons_sizes(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                icons_size = page.get_icons_sizes()
                icons_size_changes = page.check_size_changes_of_icons()
                assert icons_size != 0, "The icons in the sections hasn't sizes"
                assert icons_size_changes, "Checks of changes in icon sizes have not carried out"
