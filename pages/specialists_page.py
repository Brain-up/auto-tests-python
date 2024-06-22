"""Methods for verifying web elements on the 'Specialists' page"""
import allure

from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.specialists_page_locators import SpecialistsPageLocators
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators


class SpecialistsPage(BasePage):
    locators = SpecialistsPageLocators
    locators1 = StartUnauthorizedPageLocators

    @allure.step("Open the 'Specialists' page")
    def open_specialists_page(self):
        self.driver.get(MainPageLinks.URL_SPECIALISTS_PAGE)

    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Check the page title is present in DOM")
    def check_specialists_page_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the page title is visible on the page")
    def check_specialists_page_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get content of the title on the page")
    def get_specialists_page_title_content(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Check the page text is present in DOM")
    def check_specialists_page_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step("Check the text is visible on the page")
    def check_specialists_page_text_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TEXT)

    @allure.step("Get content of the text on the page")
    def get_text_content_on_the_specialists_page(self):
        return self.get_text(self.locators.PAGE_TEXT)

    @allure.step("Check the page grid is present in DOM")
    def check_specialists_page_grid_presence(self):
        return self.element_is_present(self.locators.PAGE_GRID)

    @allure.step("Check the page grid is visible on the page")
    def check_specialists_page_grid_visibility(self):
        return self.element_is_visible(self.locators.PAGE_GRID)

    @allure.step("Get the grid size on the page")
    def get_specialists_page_grid_size(self):
        grid = self.elements_are_present(self.locators.PAGE_GRID_CONTENT)
        return len(grid)

    @allure.step("Check the card of each specialist is visible on the page")
    def check_visibility_of_specialist_cards(self):
        cards = self.elements_are_present(self.locators.PAGE_GRID_CONTENT)
        # print(len(cards))
        for card in cards:
            return card.is_displayed()

    @allure.step("Get the list of images in specialist cards on the page")
    def get_list_of_card_images(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        # print(f"\nAmount of images in cards is: {len(card_images)}")
        return card_images

    @allure.step("Check the image in each specialist card is present and visible on the page")
    def check_image_presence_and_visibility_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        for image in card_images:
            return image.is_displayed()

    @allure.step("Get the list of attribute 'src' values of images in specialist cards on the page")
    def get_images_src_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        src_list = [image.get_attribute('src') for image in card_images]
        # print(f"The attribute 'src' values of images in cards on the page are:", *src_list, sep='\n')
        return src_list

    @allure.step("Get the list of attribute 'alt' values of images in specialist cards on the page")
    def get_images_alt_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        alt_list = [image.get_attribute('alt') for image in card_images]
        # print(f"The attribute 'alt' values of images in cards on the page are:", *alt_list, sep='\n')
        return alt_list

    @allure.step("""Get the list of size values of images in specialist cards on the page 
                    and check their changes after resizing""")
    def check_size_changes_of_card_images(self):
        card_images = self.get_list_of_card_images()
        image_sizes_before = [image.size for image in card_images]
        self.driver.set_window_size(1200, 800)
        image_sizes_after = [image.size for image in card_images]
        # print("The results of checking changes of image sizes in cards after resizing are:")
        changed, lost, unchanged = 0, 0, 0
        for i in range(len(image_sizes_after)):
            if image_sizes_before[i] != image_sizes_after[i]:
                changed += 1
                if image_sizes_after[i] == {'height': 0, 'width': 0}:
                    lost += 1
                    # print(f"\n   The image #{i + 1} has become invisible because has sizes that changed: "
                    #       f"\nfrom {image_sizes_before[i]} before resizing \nto {image_sizes_after[i]} after resizing")
                # else:
                #     print(f"\n   The image #{i + 1} has sizes that changed: \nfrom {image_sizes_before[i]} before "
                #           f"resizing \nto {image_sizes_after[i]} after resizing")
            else:
                unchanged += 1
                # print(f"\n   The image #{i + 1} has sizes that remain: \nthe same {image_sizes_before[i]} before resizing "
                #       f"\nand {image_sizes_after[i]} after resizing")
        # print(f"\nSummary of image size checks\n   Amount of images with changed sizes after resizing is: {changed}, "
        #       f"\nincluding images that have become invisible on the page: {lost}")
        # print(f"   Amount of images with unchanged sizes after resizing is: {unchanged}")
        return changed, lost, unchanged

    @allure.step("Check the image is present in the 1th card")
    def check_the_1th_card_image_presence(self):
        return self.element_is_present(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Check the image is visible in the 1th card")
    def check_the_1th_card_image_visibility(self):
        return self.element_is_visible(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Get attribute 'src' of the image in the 1th card")
    def get_the_1th_card_image_src(self):
        return self.get_image_src(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Get attribute 'alt' of the image in the 1th card")
    def get_the_1th_card_image_alt(self):
        return self.get_image_alt(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Get size of the image in the 1th card")
    def get_visible_size_of_the_1th_card_image(self):
        image_size = self.get_image_size(self.locators.GRID_CARD_01_IMAGE)
        return image_size

    @allure.step("Get the list of sections with text in specialist cards on the page")
    def get_list_of_text_sections_in_cards(self):
        card_text_sections = self.elements_are_present(self.locators.GRID_CARD_TEXT_SECTIONS)
        # print(f"\nAmount of text sections in cards is: {len(card_text_sections)}")
        return card_text_sections

    @allure.step("Check the section with text in each specialist card is present and visible on the page")
    def check_presence_and_visibility_of_text_sections_in_specialist_cards(self):
        card_text_sections = self.get_list_of_text_sections_in_cards()
        for text_section in card_text_sections:
            return text_section.is_displayed()

    @allure.step("Get the list of names in specialist cards on the page")
    def get_list_of_specialist_names_in_cards(self):
        specialist_names = self.elements_are_present(self.locators.SPECIALIST_NAMES)
        # print(f"\nAmount of specialist names in cards is: {len(specialist_names)}")
        return specialist_names

    @allure.step("Check the name in each specialist card is visible on the page")
    def check_presence_and_visibility_of_names_in_specialist_cards(self):
        specialist_names = self.get_list_of_specialist_names_in_cards()
        for specialist_name in specialist_names:
            return specialist_name.is_displayed()

    @allure.step("Get the list of sections with profession in specialist cards on the page")
    def get_list_of_specialist_professions_in_cards(self):
        specialist_profession_sections = self.elements_are_present(self.locators.SPECIALIST_PROFESSION_SECTIONS)
        # print(f"\nAmount of specialist profession descriptions in cards is: {len(specialist_profession_sections)}")
        return specialist_profession_sections

    @allure.step("Check the section with profession in each specialist card is visible on the page")
    def check_presence_and_visibility_of_professions_in_specialist_cards(self):
        specialist_profession_sections = self.get_list_of_specialist_professions_in_cards()
        for specialist_profession_section in specialist_profession_sections:
            return specialist_profession_section.is_displayed()

    @allure.step("Get the list of name values in specialist cards on the page")
    def get_name_values_in_specialist_cards(self):
        specialist_names = self.get_list_of_specialist_names_in_cards()
        name_values = [name.text for name in specialist_names]
        # print(f"The name values in cards on the page are:", *name_values, sep='\n')
        return name_values

    @allure.step("Get the list of profession values in specialist cards on the page")
    def get_profession_values_in_specialist_cards(self):
        specialist_professions = self.get_list_of_specialist_professions_in_cards()
        profession_values = [profession.text for profession in specialist_professions]
        # print(f"The profession values in cards on the page are:", *profession_values, sep='\n')
        return profession_values

    @allure.step("Check the 'All Specialists' link is present in DOM")
    def check_all_specialists_link_presence(self):
        return self.element_is_present(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Check the 'All Specialists' link is visible on the page")
    def check_all_specialists_link_visibility(self):
        return self.element_is_visible(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Check the 'All Specialists' link is clickable")
    def check_all_specialists_link_clickability(self):
        return self.element_is_clickable(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Click on the 'All Specialists' link and thereby open the corresponding web page in a new tab")
    def click_all_specialists_link(self):
        self.element_is_present_and_clickable(self.locators.ALL_SPECIALISTS_LINK).click()

    @allure.step("Get text of the element on the Start Unauthorized page")
    def get_element_text_on_opened_tab_with_start_unauthorized_page(self):
        return self.get_text(self.locators1.SECTION_1_TEXT)

    @allure.step("Get attribute 'href' of the 'All Specialists' link")
    def get_all_specialists_link_href(self):
        return self.get_link_href(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Get text in the 'All Specialists' link")
    def get_text_in_all_specialists_link(self):
        return self.get_text(self.locators.ALL_SPECIALISTS_LINK)
