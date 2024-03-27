import allure

from pages.base_page import BasePage
from locators.specialists_page_locators import SpecialistsPageLocators


class SpecialistsPage(BasePage):
    locators = SpecialistsPageLocators

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
        print(len(cards))
        for card in cards:
            return card.is_displayed()

    @allure.step("Get the list of images in specialist cards on the page")
    def get_list_of_card_images(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        print(f"\nNumber of images in cards is: {len(card_images)}")
        return card_images

    @allure.step("Check the image in each specialist card is visible on the page")
    def check_image_presence_and_visibility_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        for image in card_images:
            return image.is_displayed()

    @allure.step("Get the list of attribute 'src' values of images in specialist cards on the page")
    def get_images_src_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        src_list = [image.get_attribute('src') for image in card_images]
        print(*src_list, sep='\n')
        return src_list

    @allure.step("Get the list of attribute 'alt' values of images in specialist cards on the page")
    def get_images_alt_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        alt_list = [image.get_attribute('alt') for image in card_images]
        print(*alt_list, sep='\n')
        return alt_list

    @allure.step("Get the list of size values of images in specialist cards on the page")
    def get_sizes_of_card_images(self):
        card_images = self.get_list_of_card_images()
        size_list = [image.size for image in card_images]
        print(*size_list, sep='\n')
        return size_list

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
