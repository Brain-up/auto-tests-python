import allure
from pages.specialists_page import SpecialistsPage
from test_data.specialists_page_data import SpecialistsPageData


@allure.epic("Test Specialists Page")
class TestSpecialistsPage:

    @allure.title("Verify presence, visibility and text accuracy of the title on the Specialists page")
    def test_sp_01_01_verify_specialists_page_title(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        page_title_presence = page.check_specialists_page_title_presence()
        page_title_visibility = page.check_specialists_page_title_visibility()
        page_title_text = page.get_specialists_page_title_content()
        assert page_title_presence is not None, "The title is absent in DOM"
        assert page_title_visibility, "The title is invisible on the page"
        assert page_title_text in SpecialistsPageData.specialists_page_elements_content["page_title_content"], \
               "The title content does not match the any of the valid option"

    @allure.title("Verify presence, visibility and content accuracy of the text on the Specialists page")
    def test_sp_01_02_verify_specialists_page_text(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        page_text_presence = page.check_specialists_page_text_presence()
        page_text_visibility = page.check_specialists_page_text_visibility()
        page_text_content = page.get_text_content_on_the_specialists_page()
        assert page_text_presence is not None, "The text is absent in DOM"
        assert page_text_visibility, "The text is invisible on the page"
        assert page_text_content in SpecialistsPageData.specialists_page_elements_content["page_text_content"], \
            "The text content does not match the any of the valid option"

    @allure.title("Verify presence, visibility and size of the grid on the Specialists page")
    def test_sp_01_03_verify_specialists_page_grid(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        page_grid_presence = page.check_specialists_page_grid_presence()
        page_grid_visibility = page.check_specialists_page_grid_visibility()
        page_grid_size = page.get_specialists_page_grid_size()
        print(page_grid_size)
        assert page_grid_presence is not None, "The grid is absent in DOM"
        assert page_grid_visibility, "The grid is invisible on the page"
        assert page_grid_size == SpecialistsPageData.specialists_page_grid_size, \
               "The grid size does not match the expected value"

    @allure.title("Verify visibility of cards in the grid on the Specialists page")
    def test_sp_01_04_verify_specialist_cards_visibility(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        print(driver.current_url)
        cards_visibility = page.check_visibility_of_specialist_cards()
        assert cards_visibility, "Specialist cards are invisible in the grid"
