import random
import allure
from locators.locators import BasePageLocators, RegistrationPageLocators
from pages.base_page import BasePage
from test_data.links import MainPageLinks


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators
    links = MainPageLinks

    @allure.step("Open registration page")
    def open_registration_page(self):
        self.element_is_present_and_clickable(BasePageLocators.REGISTRATION_BUTTON).click()

    @allure.step("Fill first name")
    def fill_first_name(self, firstname):
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)

    @allure.step("Fill birthday")
    def fill_birthday(self, birthday):
        self.element_is_visible(self.locators.BIRTHDAY).send_keys(birthday)

    @allure.step("Choose gender")
    def choose_gender(self):
        gender = random.choice([self.locators.MALE, self.locators.FEMALE])
        self.element_is_clickable(gender).click()

    @allure.step("Fill email")
    def fill_email(self, email):
        self.element_is_visible(self.locators.EMAIL).send_keys(email)

    @allure.step("Fill password")
    def fill_password(self, password):
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)

    @allure.step("Fill repeat password")
    def fill_repeat_password(self, repeat_password):
        self.element_is_visible(self.locators.REPEAT_PASSWORD).send_keys(repeat_password)

    @allure.step("Choose agreement")
    def choose_agreement(self):
        self.element_is_clickable(self.locators.AGREEMENT).click()

    @allure.step("Click REGISTRATION button")
    def click_registration_button(self):
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()

    @allure.step("Check error message")
    def check_error_message_existing_email(self):
        return self.element_is_clickable(self.locators.ERROR_MESSAGE_EXISTING_EMAIL).text

    @allure.step("Wait changing url")
    def check_change_url(self):
        return self.wait_changed_url(self.links.URL_REGISTRATION_PAGE)
