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
            print(driver.current_url)
            page_title_presence = page.check_used_resources_page_title_presence()
            page_title_visibility = page.check_used_resources_page_title_visibility()
            page_title_text = page.get_used_resources_page_title_content()
            print(page_title_text)
            assert page_title_presence is not None, "The title is absent in DOM"
            assert page_title_visibility, "The title is invisible on the page"
            assert page_title_text in UsedResourcesPageData.used_resources_page_elements_content["page_title_content"], \
                "The title content does not match the any of the valid option"

        @allure.title("Verify presence, visibility and content accuracy of the text on the page")
        def test_ur_01_02_verify_used_resources_page_text(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            page_text_presence = page.check_used_resources_page_text_presence()
            page_text_visibility = page.check_used_resources_page_text_visibility()
            page_text_content = page.get_text_content_on_the_used_resources_page()
            print(page_text_content)
            assert page_text_presence is not None, "The text is absent in DOM"
            assert page_text_visibility, "The text is invisible on the page"
            assert page_text_content in UsedResourcesPageData.used_resources_page_elements_content["page_text_content"], \
                "The text content does not match the any of the valid option"

        @allure.title("Verify presence and visibility of the section with links on the page")
        def test_ur_01_03_verify_links_section_on_used_resources_page(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            links_section_presence = page.check_presence_of_links_section_on_used_resources_page()
            links_section_visibility = page.check_visibility_of_links_section_on_used_resources_page()
            assert links_section_presence is not None, "The section with links is absent in DOM"
            assert links_section_visibility, "The section with links is invisible on the page"

        @allure.title("Verify presence and visibility of the section with the freepik.com link on the page")
        def test_ur_01_04_verify_section_of_freepik_com_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            section_presence = page.check_presence_of_freepik_com_link_section()
            section_visibility = page.check_visibility_of_freepik_com_link_section()
            assert section_presence is not None, "The section with the freepik.com link is absent"
            assert section_visibility, "The section with the freepik.com link is invisible"

        @allure.title("Verify presence, visibility, clickability, href, status code, text of the freepik.com link")
        def test_ur_01_05_verify_freepik_com_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            link_presence = page.check_freepik_com_link_presence()
            link_visibility = page.check_freepik_com_link_visibility()
            link_clickability = page.check_freepik_com_link_clickability()
            link_href = page.get_freepik_com_link_href()
            print(link_href)
            link_status_code = requests.head(link_href).status_code
            print(link_status_code)
            actual_link_text = page.get_text_in_freepik_com_link()
            print(actual_link_text)
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
