import allure
from pages.used_resources_page import UsedResourcesPage
from locators.used_resources_page_locators import UsedResourcesPageLocators
from test_data.used_resources_page_data import UsedResourcesPageData


@allure.epic("Test Used Resources Page")
class TestUsedResourcesPage:

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

