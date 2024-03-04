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
            print(driver.current_url)
            page.click_freepik_com_link()
            page.switch_to_new_window()
            print(driver.current_url)
            text_on_opened_tab = page.get_element_text_on_opened_freepik_com_tab()
            assert text_on_opened_tab == \
                   UsedResourcesPageData.used_resources_page_related_elements_text["freepik_com_start_page_text"], \
                   "The freepik.com link leads to an incorrect page after click " \
                   "or opened page does not load correctly"

        @allure.title("Verify presence, visibility and accuracy of the icon in the freepik.com link's section")
        def test_ur_01_07_verify_icon_in_freepik_com_section(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            icon_presence = page.check_icon_presence_in_freepik_com_section()
            icon_visibility = page.check_icon_visibility_in_freepik_com_section()
            icon_xmlns = page.get_icon_xmlns_in_freepik_com_section()
            assert icon_presence is not None, "The icon in the freepik.com link's section is absent"
            assert icon_visibility, "The icon in the freepik.com link's section is invisible"
            assert icon_xmlns, "The 'xmlns' attribute value of the icon in the freepik.com link's section is empty"
            assert icon_xmlns == UsedResourcesPageData.icons_xmlns["icons_xmlns_on_used_resources_page"], \
                "The 'xmlns' attribute value of the icon in the freepik.com link's section is unaccurate"

        @allure.title("Verify sizes of the icon in the freepik.com link's section")
        def test_ur_01_08_verify_sizes_of_icon_in_freepik_com_section(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            icon_width = page.get_width_of_icon_in_freepik_com_section()
            icon_height = page.get_height_of_icon_in_freepik_com_section()
            print(f"The icon sizes are: {icon_width}x{icon_height} px")
            assert icon_width != 0, "The icon in the freepik.com link's section hasn't width"
            assert icon_height != 0, "The icon in the freepik.com link's section hasn't height"

        @allure.title("Verify presence and visibility of the section with the 'Plants' link on the page")
        def test_ur_01_09_verify_section_of_plants_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            section_presence = page.check_presence_of_plants_link_section()
            section_visibility = page.check_visibility_of_plants_link_section()
            assert section_presence is not None, "The section with the 'Plants' link is absent"
            assert section_visibility, "The section with the 'Plants' link is invisible"

        @allure.title("Verify presence, visibility, clickability, href, status code, text of the 'Plants' link")
        def test_ur_01_10_verify_plants_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            link_presence = page.check_plants_link_presence()
            link_visibility = page.check_plants_link_visibility()
            link_clickability = page.check_plants_link_clickability()
            link_href = page.get_plants_link_href()
            print(link_href)
            link_status_code = requests.head(link_href).status_code
            print(link_status_code)
            actual_link_text = page.get_text_in_plants_link()
            print(actual_link_text)
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
            print(driver.current_url)
            page.click_plants_link()
            page.switch_to_new_window()
            print(driver.current_url)
            text_on_opened_tab = page.get_element_text_on_opened_plants_tab()
            print(text_on_opened_tab)
            assert text_on_opened_tab == \
                   UsedResourcesPageData.used_resources_page_related_elements_text["plants_page_text"], \
                   "The 'Plants' link leads to an incorrect page after click " \
                   "or opened page does not load correctly"

        @allure.title("Verify presence, visibility and accuracy of the icon in the 'Plants' link's section")
        def test_ur_01_12_verify_icon_in_plants_section(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            icon_presence = page.check_icon_presence_in_plants_section()
            icon_visibility = page.check_icon_visibility_in_plants_section()
            icon_xmlns = page.get_icon_xmlns_in_plants_section()
            assert icon_presence is not None, "The icon in the 'Plants' link's section is absent"
            assert icon_visibility, "The icon in the 'Plants' link's section is invisible"
            assert icon_xmlns, "The 'xmlns' attribute value of the icon in the 'Plants' link's section is empty"
            assert icon_xmlns == UsedResourcesPageData.icons_xmlns["icons_xmlns_on_used_resources_page"], \
                "The 'xmlns' attribute value of the icon in the 'Plants' link's section is unaccurate"

        @allure.title("Verify sizes of the icon in the 'Plants' link's section")
        def test_ur_01_13_verify_sizes_of_icon_in_plants_section(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            print(driver.current_url)
            icon_width = page.get_width_of_icon_in_plants_section()
            icon_height = page.get_height_of_icon_in_plants_section()
            print(f"The icon sizes are: {icon_width}x{icon_height} px")
            assert icon_width != 0, "The icon in the 'Plants' link's section hasn't width"
            assert icon_height != 0, "The icon in the 'Plants' link's section hasn't height"
