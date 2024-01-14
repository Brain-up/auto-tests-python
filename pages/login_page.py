# import os
# import allure
# from dotenv import load_dotenv
# from locators.login_page_locators import LoginPageLocators
# from locators.main_page_locators import MainPageLocators
# from pages.base_page import BasePage
# from test_data.links import MainPageLinks
#
# load_dotenv()
#
#
# class LoginPage(BasePage):
#     locators = {'LoginPageLocators': LoginPageLocators(), 'MainPageLocators': MainPageLocators()}
#
#     def login_user(self):
#         with allure.step(f'Check expected link {MainPageLinks.URL_GROUPS_PAGE}'):
#             self.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
#         with allure.step(f'Check current url is: {self.driver.current_url}.'):
#             return self.driver.current_url
#
#     def login_user1(self):
#         with allure.step('Click "Login" button.'):
#             self.element_is_present_and_clickable(self.locators['MainPageLocators'].LOGIN_BUTTON).click()
#         self.check_expected_link(MainPageLinks.URL_LOGIN_PAGE)
#         with allure.step('Enter "Login" and "Password".'):
#             self.element_is_present(self.locators['LoginPageLocators'].INPUT_LOGIN).send_keys(
#                 os.environ["SPECIALIST_LOGIN"])
#             self.element_is_present(self.locators['LoginPageLocators'].INPUT_PASSWORD).send_keys(
#                 os.environ["PASSWORD"])
#         with allure.step('Click button "Sign in".'):
#             self.element_is_present_and_clickable(self.locators['LoginPageLocators'].SIGN_IN_BUTTON).click()
#             self.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
#         with allure.step(f'Check current url is: {self.driver.current_url}.'):
#             return self.driver.current_url
