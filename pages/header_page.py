"""Methods for verifying web elements in the Header of the site"""
import time
import allure
import requests
from pages.base_page import BasePage
from locators.header_page_locators import (HeaderUnauthorizedLocators, HeaderAuthorizedLocators,
                                           StartUnauthorizedPageLocators)


class HeaderPage(BasePage):
    locators = HeaderUnauthorizedLocators
    locators1 = HeaderAuthorizedLocators
    locators2 = StartUnauthorizedPageLocators

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
        tags = [element.tag_name for element in elements]
        # print(tags)
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level_in_header(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting the Header")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(tags)
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_in_header(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting the Header")
    def get_structure_of_3rd_level(self):
        time.sleep(5)
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(tags)
        return self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)

    @allure.step("Check if elements on the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level_in_header(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting the Header")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(tags)
        return elements

    @allure.step("Check if elements on the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level_in_header(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting the Header")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(tags)
        return elements

    @allure.step("Check if elements on the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level_in_header(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level()[1:4])

    @allure.step("Get structure of the 6th level of nesting the Header")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(tags)
        return elements

    @allure.step("Check if elements on the 6th level of nesting are invisible")
    def check_elements_invisibility_on_6th_level_in_header(self):
        return all(self.element_is_not_visible(element) for element in self.get_structure_of_6th_level()[:6])

    @allure.step("Get the list of links on different levels of nesting in the Header for an unauthorized user")
    def get_list_of_links_unauth(self):
        return self.elements_are_present(self.locators.HEADER_LINKS_UNAUTH)

    @allure.step("Get the list of links on different levels of nesting in the Header for an authorized user")
    def get_list_of_links_auth(self):
        return self.elements_are_present(self.locators.HEADER_LINKS_AUTH)

    @allure.step("""Get the list of the 'About', 'Telegram', 'Registration', 'Logo' links (direct links) in the Header 
                 for an unauthorized user""")
    def get_list_of_direct_links_unauth(self):
        links = self.get_list_of_links_unauth()
        direct_links = []
        for i in [1, 2, 9, 0]:
            direct_links.append(links[i])
        return direct_links

    @allure.step("""Get the list of the 'Groups', 'Statistics', 'About', 'Telegram', 'Profile', 'Logo' links 
                    (direct links) in the Header for an authorized user""")
    def get_list_of_direct_links_auth(self):
        links = self.get_list_of_links_auth()
        direct_links = []
        for i in [1, 2, 3, 4, 11, 0]:
            direct_links.append(links[i])
        return direct_links

    @allure.step("Check the 'About', 'Telegram', 'Registration', 'Logo' links are visible for an unauthorized user")
    def check_direct_links_visibility_unauth(self):
        return all(link.is_displayed() for link in self.get_list_of_direct_links_unauth())

    @allure.step("""Check the 'Groups', 'Statistics', 'About', 'Telegram', 'Registration', 'Logo' links are visible "
                 for an authorized user""")
    def check_direct_links_visibility_auth(self):
        return all(link.is_displayed() for link in self.get_list_of_direct_links_auth())

    @allure.step("""Get the list of the 'Contacts', 'Specialists', 'Contributors', 'Used Resources', "
                  'Donate', 'GitHub' links in the 'More' dropdown in the Header for every user""")
    def get_list_of_links_in_more1(self):
        links = self.get_list_of_links_unauth()
        more_links = []
        for i in range(3, 9):
            more_links.append(links[i])
        return more_links

    @allure.step("""Get the list of links (internal and external) in the 'More' dropdown in the Header
                 for every user""")
    def get_list_of_links_in_more(self):
        return self.elements_are_present(self.locators.LINKS_IN_MORE)

    @allure.step("""Check the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links 
                    in the 'More' dropdown are invisible for every user""")
    def check_links_invisibility_in_more(self):
        return all(self.element_is_not_visible(element) for element in self.get_list_of_links_in_more())

    @allure.step("""Check the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links 
                    in the 'More' dropdown are visible for every user""")
    def check_links_visibility_in_more(self):
        self.click_more_button()
        return all(link.is_displayed() for link in self.get_list_of_links_in_more())

    # Lists of links
    @allure.step("""Get the list of the 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links "
                  (internal links) in the 'More' dropdown for every user""")
    def get_list_of_internal_links_in_more(self):
        return self.get_list_of_links_in_more()[2:]

    @allure.step("""Get the list of the 'Donate', 'GitHub' links (external links) 
                    in the 'More' dropdown for every user""")
    def get_list_of_external_links_in_more(self):
        return self.get_list_of_links_in_more()[:2]

    @allure.step("Get the general list of internal links in the Header for an unauthorized user""")
    def get_list_of_internal_links(self):
        links = self.get_list_of_links_unauth()
        internal_links = []
        for i in [0, 1, 5, 6, 7, 8, 9]:
            internal_links.append(links[i])
        return internal_links

    @allure.step("Get the general list of external links in the Header for an unauthorized user""")
    def get_list_of_external_links(self):
        links = self.get_list_of_links()
        external_links = []
        for i in [2, 3, 4]:
            external_links.append(links[i])
        return external_links

    @allure.step("""Get the list of the 'About', 'Registration', 'Logo' links (direct internal links) 
    in the Header for an unauthorized user""")
    def get_list_of_direct_internal_links_unauth(self):
        links = self.get_list_of_links_unauth()
        direct_internal_links = []
        for i in [1, 9, 0]:
            direct_internal_links.append(links[i])
        return direct_internal_links

    @allure.step("""Get the list of the 'Statistics', 'Groups', 'About', 'Profile', 'Logo' links (direct internal links)
     in the Header for an authorized user""")
    def get_list_of_direct_internal_links_auth(self):
        links = self.get_list_of_links_auth()
        direct_internal_links = []
        for i in [2, 1, 3, 11, 0]:
            direct_internal_links.append(links[i])
        print([element.get_attribute("href") for element in direct_internal_links])
        return direct_internal_links

    @allure.step("""Get the list of the 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links "
                 (internal links) in the 'More' dropdown for an unauthorized user""")
    def get_list_of_internal_links_in_more1(self):
        links = self.get_list_of_links_unauth()
        more_internal_links = []
        for i in range(5, 9):
            more_internal_links.append(links[i])
        return more_internal_links

    @allure.step("""Get the list of the 'Donate', 'GitHub' links (external links) in the 'More' dropdown 
                    for an unauthorized user""")
    def get_list_of_external_links_in_more1(self):
        links = self.elements_are_present(self.locators.HEADER_LINKS_UNAUTH)
        external_links = []
        for i in range(3, 5):
            external_links.append(links[i])
        return external_links

    @allure.step("Check the 'Logo' link is present in the Header for every user")
    def check_logo_link_presence(self):
        return self.element_is_present(self.locators.LOGO_LINK)

    @allure.step("Check the 'Logo' link is visible for every user")
    def check_logo_link_visibility(self):
        return self.element_is_visible(self.locators.LOGO_LINK)

    @allure.step("Check the 'Registration' link is present in the Header for an unauthorized user")
    def check_registration_link_presence(self):
        return self.element_is_present(self.locators.LINK_REGISTRATION)

    @allure.step("Check the 'Registration' link is visible for an unauthorized user")
    def check_registration_link_visibility(self):
        return self.element_is_visible(self.locators.LINK_REGISTRATION)

    @allure.step("Check the 'Profile' link is present in the Header for an authorized user")
    def check_profile_link_presence(self):
        return self.element_is_present(self.locators1.LINK_PROFILE)

    @allure.step("Check the 'Profile' link is visible for an authorized user")
    def check_profile_link_visibility(self):
        return self.element_is_visible(self.locators1.LINK_PROFILE)

    @allure.step("Get the list of buttons in the Header for an unauthorized user")
    def get_list_of_buttons_unauth(self):
        return self.elements_are_present(self.locators.HEADER_BUTTONS)

    @allure.step("Check buttons are visible for an unauthorized user")
    def check_buttons_unauth_visibility(self):
        return all(button.is_displayed() for button in self.get_list_of_buttons_unauth())

    @allure.step("Get the list of buttons in the Header for an authorized user")
    def get_list_of_buttons_auth(self):
        return self.elements_are_present(self.locators.HEADER_BUTTONS)[:4]


    @allure.step("Check buttons are visible are visible for an authorized user")
    def check_buttons_auth_visibility(self):
        return all(button.is_displayed() for button in self.get_list_of_buttons_auth())

    @allure.step("Get the list of 'ru' and 'en' buttons in the Header for unauthorized and authorized users")
    def get_list_of_ru_en_buttons(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.RU_EN_BUTTONS)

    @allure.step("Check if 'ru' and 'en' buttons are visible for unauthorized and authorized users")
    def check_ru_en_buttons_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_ru_en_buttons())

    @allure.step("Check the 'More' button is present in the Header for unauthorized and authorized users")
    def check_more_button_presence(self):
        return self.element_is_present(self.locators.MORE_BUTTON)

    @allure.step("Check the 'More' button is visible for unauthorized and authorized users")
    def check_more_button_visibility(self):
        return self.element_is_visible(self.locators.MORE_BUTTON)

    @allure.step("Check the 'Logout' button is present in the Header for an authorized user")
    def check_logout_button_presence(self):
        return self.element_is_present(self.locators1.LOGOUT_BUTTON)

    @allure.step("Check the 'Logout' button is visible for an authorized user")
    def check_logout_button_visibility(self):
        return self.element_is_visible(self.locators1.LOGOUT_BUTTON)

    # Checks of text in the Header
    @allure.step("Get text in the 'About', 'Telegram', 'Registration' links in the Header for an unauthorized user")
    def get_text_in_direct_links_unauth(self):
        return [link.text for link in self.get_list_of_direct_links_unauth()[:3]]

    @allure.step("""Get text in the 'Groups', 'Statistics', 'About', 'Telegram', 'Profile' links in the Header 
    for an authorized user""")
    def get_text_in_direct_links_auth(self):
        return [link.text for link in self.get_list_of_direct_links_auth()[:5]]

    @allure.step("""Get text in the 'Donate', 'GitHub', 'Contacts', 'Specialists', 'Contributors', 'Used Resources'  
    links in the Header""")
    def get_text_of_links_in_more(self):
        self.click_more_button()
        return [link.text for link in self.get_list_of_links_in_more()]

    @allure.step("Get text in buttons in the Header for an unauthorized user")
    def get_text_in_buttons_unauth(self):
        return [button.text for button in self.get_list_of_buttons_unauth()]

    @allure.step("Get text in buttons in the Header for an authorized user")
    def get_text_in_buttons_auth(self):
        return [button.text for button in self.get_list_of_buttons_auth()[:3]]

    @allure.step("Get text in 'ru' and 'en' buttons in the Header")
    def get_text_in_ru_en_buttons(self):
        return [button.text for button in self.get_list_of_ru_en_buttons()]

    # Checks of links in the Header
    @allure.step("Check if links are clickable in the Header for an unauthorized user")
    def check_links_clickability_unauth(self):
        return all(link.is_enabled() for link in self.get_list_of_links_unauth())

    @allure.step("Check if links are clickable in the Header for an authorized user")
    def check_links_clickability_auth(self):
        return all(link.is_enabled() for link in self.get_list_of_links_auth())

    @allure.step("Get attribute 'href' of links in the Header for an unauthorized user")
    def get_links_href_unauth(self):
        return [element.get_attribute("href") for element in self.get_list_of_links_unauth()]

    @allure.step("Get attribute 'href' of links in the Header for an authorized user")
    def get_links_href_auth(self):
        return [element.get_attribute("href") for element in self.get_list_of_links_auth()]

    @allure.step("Get status codes of links in the Header for an unauthorized user")
    def get_links_status_codes_unauth(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href_unauth()]

    @allure.step("Get status codes of links in the Header for an authorized user")
    def get_links_status_codes_auth(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href_auth()]

    # Checks of links navigation
    @allure.step("""Click on internal links in the Header and thereby open corresponding web pages in the same tab 
    for an unauthorized user""")
    def click_on_internal_links_in_header_unauth(self):
        opened_pages = []
        # Click on the 'About', 'Registration', 'Logo' links
        for link in self.get_list_of_direct_internal_links_unauth():
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

    @allure.step("""Click on internal links in the Header and thereby open corresponding web pages in the same tab 
    for an authorized user""")
    def click_on_internal_links_in_header_auth(self):
        opened_pages = []
        # Click on the 'Statistics', 'Groups', 'About', 'Profile', 'Logo' links
        for link in self.get_list_of_direct_internal_links_auth():
            link.click()
            time.sleep(1)
            opened_pages.append(self.get_current_tab_url())
        # Click on the 'Contacts', 'Specialists', 'Contributors', 'Used Resources' links
        for link in self.get_list_of_internal_links_in_more():
            self.click_more_button()
            time.sleep(1)
            link.click()
            time.sleep(1)
            opened_pages.append(self.get_current_tab_url())
        print('\n', *opened_pages, sep='\n')
        return opened_pages

    @allure.step("""Click on external links in the Header and thereby open corresponding web pages on new tabs 
    for every user""")
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

    @allure.step("Click on the 'Logo' link for every user")
    def click_on_logo_link(self):
        self.element_is_present_and_clickable(self.locators.LOGO_LINK).click()
        return self.driver.current_url

    # Checks of buttons clicking in the Header
    @allure.step("Click on the 'More' button for every user")
    def click_more_button(self):
        return self.element_is_present_and_clickable(self.locators.MORE_BUTTON).click()

    @allure.step("Check for dropdown is open/closed after clicking on the button 'More' in the Header for every user")
    def check_dropdown_opens_and_closes(self):
        dropdown_state = 0
        if self.check_links_invisibility_in_more():
            dropdown_state = 1
        if self.check_links_visibility_in_more():
            dropdown_state = 2
        self.click_more_button()
        if self.check_links_invisibility_in_more():
            dropdown_state = 3
        if dropdown_state == 3:
            return True

    @allure.step("Click on the 'ru' button")
    def click_on_ru_button(self):
        self.element_is_present_and_clickable(self.locators.RU_BUTTON).click()

    @allure.step("Click on the 'en' button")
    def click_on_en_button(self):
        self.element_is_present_and_clickable(self.locators.EN_BUTTON).click()

    @allure.step("Check for language change to RU on the page after clicking on the button 'ru'")
    def check_language_change_ru(self):
        self.click_on_ru_button()
        return self.element_is_present(self.locators2.START_UNAUTHORIZED_PAGE_TITLE).text

    @allure.step("Check for language change to EN on the page after clicking on the button 'en'")
    def check_language_change_en(self):
        self.click_on_en_button()
        return self.element_is_present(self.locators2.START_UNAUTHORIZED_PAGE_TITLE).text

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
