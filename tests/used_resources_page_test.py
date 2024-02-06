import allure
from pages.used_resources_page import UsedResourcesPage
from locators.used_resources_page_locators import UsedResourcesPageLocators


@allure.epic("Test Used Resources Page")
class TestUsedResourcesPage:

    class TestUsedResourcesPageForAuthorizedUser:
        locators = UsedResourcesPageLocators()

        @allure.title("Verify visibility and text accuracy of the page title")
        def test_ur_01_01_verify_used_resources_page_title(self, driver, default_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            page_title = page.check_used_resources_page_title_visibility()
            page_title_text = page.get_used_resources_page_title_text()
            print(page_title_text)
            assert page_title, "The page title is invisible on the page"
            assert page_title_text == "Используемые ресурсы", "The page title text does not match the expected value"
