"""Methods for verifying web elements in the Header of the site"""
import time
import allure
import requests
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    locators = HeaderPageLocators

    # Checking the structure and display of elements in the Header
    @allure.step("Check the Header is present in the DOM tree on the page")
    def check_header_presence(self):
        return self.element_is_present(self.locators.HEADER_CONTENT)

    @allure.step("Check if the Header is visible on the page")
    def check_header_visibility(self):
        return self.element_is_visible(self.locators.HEADER_CONTENT)

    @allure.step("Get structure of the 1st level of nesting in the Header")
    def get_structure_of_1st_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 1st level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting the Header")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 2nd level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting the Header")
    def get_structure_of_3rd_level(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 3rd level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting the Header")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 4th level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting the Header")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 5th level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level()[1:4])

    @allure.step("Get structure of the 6th level of nesting the Header")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 6th level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 6th level of nesting are invisible")
    def check_elements_invisibility_on_6th_level_on_page(self):
        return all(self.element_is_not_visible(element) for element in self.get_structure_of_6th_level())

    @allure.step("Get the list of links on different levels of nesting in the Header")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.HEADER_LINKS)

    @allure.step("Check the 'Logo' link is present in the Header")
    def check_logo_link_presence(self):
        return self.element_is_present(self.locators.LOGO_LINK)

    @allure.step("Check the 'Logo' link is visible")
    def check_logo_link_visibility(self):
        return self.element_is_visible(self.locators.LOGO_LINK)

    @allure.step("Get the list of links in the section 2 in the Header")
    def get_list_of_links_in_section2(self):
        return self.elements_are_present(self.locators.LINKS2)

    @allure.step("Check the 'About' and the 'Telegram' links in the section 2 are visible")
    def check_links_visibility_in_section2(self):
        return all(link.is_displayed() for link in self.get_list_of_links_in_section2())

    @allure.step("Get the list of links in the section 3 in the Header")
    def get_list_of_links_in_section3(self):
        return self.elements_are_present(self.locators.LINKS3)

    @allure.step("""Check the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links 
    in the section 3 are invisible""")
    def check_links_invisibility_in_section3(self):
        return all(self.element_is_not_visible(element) for element in self.get_list_of_links_in_section3())

    @allure.step("""Check the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links 
    in the section 3 are visible""")
    def check_links_visibility_in_section3(self):
        self.click_more_button()
        return all(link.is_displayed() for link in self.get_list_of_links_in_section3())

    @allure.step("Get the list of buttons in the Header")
    def get_list_of_buttons(self):
        return self.elements_are_present(self.locators.HEADER_BUTTONS)

    @allure.step("Check buttons are visible")
    def check_buttons_visibility(self):
        return all(button.is_displayed() for button in self.get_list_of_buttons())

    @allure.step("Get the list of 'ru' and 'en' buttons in the Header")
    def get_list_of_ru_en_buttons(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.RU_EN_BUTTONS_SECTION)

    @allure.step("Check if 'ru' and 'en' buttons are visible")
    def check_ru_en_buttons_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_ru_en_buttons())

    @allure.step("Check the 'More' button is present in the Header")
    def check_more_button_presence(self):
        return self.element_is_present(self.locators.MORE_BUTTON)

    @allure.step("Check the 'More' button is visible")
    def check_more_button_visibility(self):
        return self.element_is_visible(self.locators.MORE_BUTTON)

    @allure.step("Check the 'Registration' link is present in the Header")
    def check_registration_link_presence(self):
        return self.element_is_present(self.locators.LINK_REGISTRATION)

    @allure.step("Check the 'Registration' link is visible")
    def check_registration_link_visibility(self):
        return self.element_is_visible(self.locators.LINK_REGISTRATION)

    # Checking text in the Header
    @allure.step("Get text in the 'About' and the 'Telegram' links in the Header")
    def get_text_in_links2(self):
        return [link.text for link in self.get_list_of_links_in_section2()]

    @allure.step("""Get text in the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources'  
    links in the Header""")
    def get_text_in_links3(self):
        self.click_more_button()
        return [link.text for link in self.get_list_of_links_in_section3()]

    @allure.step("Get text in the 'Registration' link in the Header")
    def get_text_in_registration_link(self):
        return self.get_text(self.locators.LINK_REGISTRATION)

    @allure.step("Get text in buttons in the Header")
    def get_text_in_buttons(self):
        return [button.text for button in self.get_list_of_buttons()]

    @allure.step("Get text in 'ru' and 'en' buttons in the Header")
    def get_text_in_ru_en_buttons(self):
        return [button.text for button in self.get_list_of_ru_en_buttons()]

    # Checking links in the Header
    @allure.step("Check if links are clickable in the Header")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'href' of links in the Header")
    def get_links_href(self):
        return [element.get_attribute("href") for element in self.get_list_of_links()]

    @allure.step("Get status codes of links in the Header")
    def get_links_status_codes(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href()]

    # Checks on links navigation
    @allure.step("Click on the 'Logo' link")
    def click_logo_link(self):
        self.element_is_present_and_clickable(self.locators.LOGO_LINK).click()
        return self.driver.current_url

    @allure.step("Click on the 'More' button")
    def click_more_button(self):
        return self.element_is_present_and_clickable(self.locators.MORE_BUTTON).click()

    @allure.step("""Get the list of the 'About', 'Registration', 'Logo' links
                 (direct internal links) in the Header""")
    def get_list_of_direct_internal_links(self):
        links = self.get_list_of_links()
        direct_internal_links = []
        for i in [1, 9, 0]:
            direct_internal_links.append(links[i])
        return direct_internal_links

    @allure.step("""Get the list of the 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links "
                 (internal links) in the 'More' dropdown""")
    def get_list_of_internal_links_in_more(self):
        links = self.get_list_of_links()
        more_internal_links = []
        for i in range(5, 9):
            more_internal_links.append(links[i])
        return more_internal_links

    @allure.step("Get the list of the 'Donate', 'GitHub', links (external links) in the 'More' dropdown")
    def get_list_of_external_links_in_more(self):
        links = self.elements_are_present(self.locators.HEADER_LINKS)
        external_links = []
        for i in range(3, 5):
            external_links.append(links[i])
        return external_links

    @allure.step("Click on internal links in the Header and thereby open corresponding web pages in the same tab")
    def click_on_internal_links_in_header(self):
        opened_pages = []
        # Click on the 'About', 'Registration', 'Logo' links
        for link in self.get_list_of_direct_internal_links():
            link.click()
            opened_pages.append(self.get_current_tab_url())
        # Click on the 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links
        for link in self.get_list_of_internal_links_in_more():
            self.click_more_button()
            link.click()
            time.sleep(1)
            opened_pages.append(self.get_current_tab_url())
        print('\n', *opened_pages, sep='\n')
        return opened_pages

    @allure.step("Click on external links in the Header and thereby open corresponding web pages on new tabs")
    def click_on_external_links_in_header(self):
        opened_pages = []
        # Click on the 'Telegram' link
        self.element_is_present_and_clickable(self.locators.LINK_TELEGRAM).click()
        # Click on the 'GitHub', 'Donate' links
        self.click_more_button()
        new_tabs = [link.click() for link in self.get_list_of_external_links_in_more()]
        # Get the list of opened tabs urls
        for i in range(1, len(new_tabs) + 2):
            self.driver.switch_to.window(self.driver.window_handles[i])
            opened_pages.append(self.get_current_tab_url())
        print('\n', *opened_pages, sep='\n')
        return opened_pages

    # Separated checks of links navigation
    @allure.step("""Click on the 'About', 'Telegram', 'Registration' links in the Header 
    and thereby open corresponding web pages in the same or new tab""")
    def click_on_links_and_return_back(self):
        opened_pages = []
        # Click on the 'About' link and return back
        self.element_is_present_and_clickable(self.locators.LINK_ABOUT).click()
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)
        # Click on the 'Telegram' link and return back
        self.element_is_present_and_clickable(self.locators.LINK_TELEGRAM).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        opened_pages.append(self.driver.current_url)
        self.driver.switch_to.window(self.driver.window_handles[0])
        opened_pages.append(self.driver.current_url)
        # Click on the 'Registration' link and return back
        self.element_is_present_and_clickable(self.locators.LINK_REGISTRATION).click()
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)
        print('\n', *opened_pages, sep='\n')
        return opened_pages

    @allure.step("""Click on the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links  
    in the Header and thereby open corresponding web pages in the same or new tab""")
    def click_on_links3_and_return_back(self):
        opened_pages = []
        # Click on the 'Contacts' link and return back
        self.click_more_button()
        self.element_is_present_and_clickable(self.locators.LINK_CONTACTS).click()
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)
        # Click on the 'Specialists' link and return back
        self.click_more_button()
        self.element_is_present_and_clickable(self.locators.LINK_SPECIALISTS).click()
        time.sleep(3)
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)
        # Click on the 'Contributors' link and return back
        self.click_more_button()
        self.element_is_present_and_clickable(self.locators.LINK_CONTRIBUTORS).click()
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)
        # Click on the 'Used Resources' link and return back
        self.click_more_button()
        self.element_is_present_and_clickable(self.locators.LINK_USED_RESOURCES).click()
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)

        # Click on the 'Donate' link and return back
        self.click_more_button()
        self.element_is_present_and_clickable(self.locators.LINK_DONATE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        opened_pages.append(self.driver.current_url)
        self.driver.switch_to.window(self.driver.window_handles[0])
        opened_pages.append(self.driver.current_url)
        # Click on the 'GitHub' link and return back
        self.element_is_present_and_clickable(self.locators.LINK_GITHUB).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[2])
        opened_pages.append(self.driver.current_url)
        self.driver.switch_to.window(self.driver.window_handles[0])
        opened_pages.append(self.driver.current_url)
        print('\n', *opened_pages, sep='\n')
        return opened_pages

    # Checking images in the Header
    @allure.step("Check if the 'Logo' image is present")
    def check_logo_image_presence(self):
        return self.element_is_present(self.locators.LOGO_IMAGE)

    @allure.step("Check if the 'Logo' image is visible")
    def check_logo_image_visibility(self):
        return self.element_is_visible(self.locators.LOGO_IMAGE)

    @allure.step("Get attribute 'xmlns' of the 'Logo' image")
    def get_xmlns_of_logo_image(self):
        return self.element_is_present(self.locators.LOGO_IMAGE).get_attribute("xmlns")

    @allure.step("Get size of the 'Logo' image")
    def get_size_of_logo_image(self):
        return self.get_image_size(self.locators.LOGO_IMAGE)

    @allure.step("""Check if size of the 'Logo' image changes after resizing""")
    def check_size_changes_of_logo_image(self):
        image_size_before = self.get_size_of_logo_image()
        self.driver.set_window_size(220, 1100)
        image_size_after = self.get_size_of_logo_image()
        changes = 1 if image_size_before == image_size_after else 0
        print("\nAn image size is not changed after resizing" if changes == 1 else "\nThe 'Logo' image size is changed")
        return changes
