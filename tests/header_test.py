"""Auto tests for verifying web elements in the Header of the site"""
import allure
from pages.header_page import HeaderPage as hPage
from test_data.header_data import HeaderData as hPD


@allure.epic("Test Header")
class TestHeaderPage:
    class TestUnauthorizedHeaderPage:
        class TestUnHdPageStructure:
            @allure.title("Verify presence and visibility of the Header for an unauthorized user")
            def test_hpu_01_01_verify_unauth_header_presence_and_visibility(self, driver, main_page_open):
                page = hPage(driver)
                page_content_presence = page.check_header_presence()
                page_content_visibility = page.check_header_visibility()
                assert page_content_presence, "The Header is absent in DOM"
                assert page_content_visibility, "The Header is invisible for an unauthorized user"

            @allure.title("""Verify composition, visibility of elements on the 1st-6th levels of nesting in the Header
            for an unauthorized user""")
            def test_hpu_01_02_verify_unauth_header_structure_and_visibility(self, driver, main_page_open):
                page = hPage(driver)
                structure_of_1st_level = page.get_structure_of_1st_level()
                visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_header()
                structure_of_2nd_level = page.get_structure_of_2nd_level()
                visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_header()
                structure_of_3rd_level = page.get_structure_of_3rd_level()
                visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_in_header()
                structure_of_4th_level = page.get_structure_of_4th_level()
                visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_in_header()
                structure_of_5th_level = page.get_structure_of_5th_level()
                visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_in_header()
                structure_of_6th_level = page.get_structure_of_6th_level()
                invisibility_of_elements_on_6th_level = page.check_elements_invisibility_on_6th_level_in_header()
                assert structure_of_1st_level, "The Header is empty"
                assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
                assert structure_of_2nd_level, "Elements on the 2nd level are absent in the Header"
                assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
                assert structure_of_3rd_level, "Elements on the 3rd level are absent in the Header"
                assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
                assert structure_of_4th_level, "Elements on the 4th level are absent in the Header"
                assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
                assert structure_of_5th_level, "Elements on the 5th level are absent in the Header"
                assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"
                assert structure_of_6th_level, "Elements on the 6th level are absent in the Header"
                assert invisibility_of_elements_on_6th_level, "6th-level elements are visible"

            @allure.title("Verify presence, visibility of links, buttons in the Header for an unauthorized user")
            def test_hpu_01_03_verify_unauth_header_structural_elements(self, driver, main_page_open):
                page = hPage(driver)
                header_links = page.get_list_of_links_unauth()
                header_direct_links = page.get_list_of_direct_links_unauth()
                header_direct_links_visibility = page.check_direct_links_visibility_unauth()
                links_in_more_presence = page.get_list_of_links_in_more()
                links_in_more_invisibility = page.check_links_invisibility_in_more()
                links_in_more_visibility = page.check_links_visibility_in_more()
                logo_link_presence = page.check_logo_link_presence()
                logo_link_visibility = page.check_logo_link_visibility()
                registration_link_presence = page.check_registration_link_presence()
                registration_link_visibility = page.check_registration_link_visibility()
                buttons_presence = page.get_list_of_buttons_unauth()
                buttons_visibility = page.check_buttons_unauth_visibility()
                ru_en_buttons_presence = page.get_list_of_ru_en_buttons()
                ru_en_buttons_visibility = page.check_ru_en_buttons_visibility()
                more_button_presence = page.check_more_button_presence()
                more_button_visibility = page.check_more_button_visibility()
                assert header_links, "Links are absent in the Header"
                assert header_direct_links, "Direct links are absent in the Header"
                assert header_direct_links_visibility, "Direct links are invisible"
                assert links_in_more_presence, "Links in the dropdown 'More' are absent in the Header"
                assert links_in_more_invisibility, "Links in the dropdown 'More' are visible"
                assert links_in_more_visibility, "Links in the dropdown 'More' are invisible"
                assert logo_link_presence, "The 'Logo' link is absent in the Header"
                assert logo_link_visibility, "The 'Logo' link is invisible"
                assert registration_link_presence, "The 'Registration' link is in the Header"
                assert registration_link_visibility, "The 'Registration' link is invisible"
                assert buttons_presence, "Buttons are absent in the Header"
                assert buttons_visibility, "Buttons are invisible"
                assert ru_en_buttons_presence, "The 'ru' and 'en' buttons are absent in the Header"
                assert ru_en_buttons_visibility, "The 'ru' and 'en' buttons are invisible"
                assert more_button_presence, "The 'More' button is absent in the Header"
                assert more_button_visibility, "The 'More' button is invisible"

        class TestUnHdPageText:
            @allure.title("Verify values of the text in links, buttons in the Header for an unauthorized user")
            def test_hpu_02_01_verify_unauth_text_in_links_and_buttons(self, driver, main_page_open):
                page = hPage(driver)
                direct_links_text = page.get_text_in_direct_links_unauth()
                links_in_more_text = page.get_text_of_links_in_more()
                buttons_text = page.get_text_in_buttons_unauth()
                ru_en_buttons_text = page.get_text_in_ru_en_buttons()
                assert all(element in hPD.links_text_unauth for element in direct_links_text), \
                    "Text in links in section 2 mismatches valid values"
                assert all(element in hPD.links_text_unauth for element in links_in_more_text), \
                    "Text in links in section 3 mismatches valid values"
                assert all(element in hPD.buttons_text for element in buttons_text), \
                    "Text in buttons mismatches valid values"
                assert all(element in hPD.ru_en_buttons_text for element in ru_en_buttons_text), \
                    "Text in 'ru-en' buttons mismatches valid values"

        class TestUnHdPageLinks:
            @allure.title("Verify clickability, href, status code of links in the Header for an unauthorized user")
            def test_hpu_03_01_verify_unauth_header_links(self, driver, main_page_open):
                page = hPage(driver)
                links_clickability = page.check_links_clickability_unauth()
                tg_link_title = page.get_tg_link_title()
                links_href = page.get_links_href_unauth()
                link_status_codes = page.get_links_status_codes_unauth()
                assert links_clickability, "Links are unclickable"
                assert tg_link_title, "The link title value is empty"
                assert tg_link_title in hPD.link_titles, "The link title mismatches the valid value"
                assert links_href, "Links href are empty"
                assert all(element in hPD.set_unauth for element in links_href), \
                    "Attributes 'href' of links mismatch valid values"
                assert all(element in hPD.link_status_codes for element in link_status_codes), \
                    "Status codes of links mismatch valid values"

            @allure.title("""Verify if internal links in the Header for an unauthorized user 
            lead to correct pages after click""")
            def test_hpu_03_02_verify_unauth_internal_links_lead_to_correct_pages(self, driver, main_page_open):
                page = hPage(driver)
                internal_links_in_more = page.get_list_of_internal_links_in_more()
                opened_pages = page.click_on_internal_links_in_header_unauth()
                assert internal_links_in_more, "Internal links are not collected in the list"
                assert all(element in hPD.set_unauth for element in opened_pages), \
                    "Some of internal links lead to incorrect pages after clicking"

            @allure.title("""Verify if external links in the Header for an unauthorized user 
            lead to correct pages after click""")
            def test_hpu_03_03_verify_unauth_external_links_lead_to_correct_pages(self, driver, main_page_open):
                page = hPage(driver)
                external_links_in_more = page.get_list_of_external_links_in_more()
                opened_pages = page.click_on_external_links_in_header()
                assert external_links_in_more, "External links are not collected in the list"
                assert all(element in hPD.set_unauth for element in opened_pages), \
                    "Some of external links lead to incorrect pages after clicking"

            @allure.title("""Verify that the 'Logo' link on the Start Unauthorized Page 
                             doesn't refresh the current page or lead to other pages after clicking""")
            def test_hpu_03_04_verify_click_unauth_logo_link(self, driver, main_page_open):
                page = hPage(driver)
                handles_before = driver.window_handles
                initial_page_source = page.driver.page_source
                initial_page_url = page.driver.current_url
                current_page_url = page.click_on_logo_link()
                handles_after = driver.window_handles
                current_page_source = page.driver.page_source
                assert len(handles_before) == len(handles_after), "The number of open tabs changed after clicking"
                assert initial_page_source == current_page_source, \
                    "Logo link in the Header refreshes the page after clicking"
                assert initial_page_url == current_page_url, "Logo link in the Header leads to some page after clicking"

            @allure.title("""Verify the dropdown opens/closes after clicking on the 'More' button in the Header 
            on the Start Unauthorized Page""")
            def test_hpu_03_05_verify_unauth_more_button_click(self, driver, main_page_open):
                page = hPage(driver)
                button_click = page.check_dropdown_opens_and_closes()
                assert button_click, "The dropdown isn't open/closed after clicking the 'More' button"

            @allure.title("Verify switching of the 'ru', 'en' buttons in the Header on the Start Unauthorized Page")
            def test_hpu_03_06_verify_unauth_ru_en_buttons_switching(self, driver, main_page_open):
                page = hPage(driver)
                text_ru = page.check_language_change_ru_unauth()
                text_en = page.check_language_change_en_unauth()
                assert text_ru == hPD.title_text_ru_unauth, "RU language isn't enabled after clicking the 'ru' button"
                assert text_en == hPD.title_text_en_unauth, "EN language isn't enabled after clicking the 'en' button"

        class TestUnHdPageImages:
            @allure.title("""Verify presence, visibility and attributes of the image in the Logo link in the Header 
               on the Start Unauthorized Page""")
            def test_hpu_04_01_verify_unauth_logo_image(self, driver, main_page_open):
                page = hPage(driver)
                logo_image_presence = page.check_unauth_logo_image_presence()
                logo_image_visibility = page.check_unauth_logo_image_visibility()
                image_xmlns = page.get_xmlns_of_unauth_logo_image()
                assert logo_image_presence, "An image in the Logo link is absent on the page"
                assert logo_image_visibility, "The Logo image is invisible"
                assert image_xmlns, "The xmlns attribute value of the Logo image is empty"
                assert image_xmlns == hPD.logo_image_xmlns, \
                    "The xmlns attribute of the Logo image mismatches valid value"

            @allure.title("Verify size of the image in the Logo link in the Header on the Start Unauthorized Page")
            def test_hpu_04_02_verify_unauth_logo_image_size(self, driver, main_page_open):
                page = hPage(driver)
                image_size = page.get_size_of_unauth_logo_image()
                image_size_change = page.check_size_changes_of_unauth_logo_image()
                assert image_size != 0, f"The image in the Logo image has not size"
                assert image_size_change, "The Logo image size is changed"

    class TestAuthorizedHeaderPage:
        class TestAuHdPageStructure:
            @allure.title("Verify presence and visibility of the Header for an authorized user")
            def test_hpa_01_01_verify_auth_header_presence_and_visibility(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                page_content_presence = page.check_header_presence()
                page_content_visibility = page.check_header_visibility()
                assert page_content_presence, "The Header is absent in DOM"
                assert page_content_visibility, "The Header is invisible for an authorized user"

            @allure.title("""Verify composition, visibility of elements on the 1st-6th levels of nesting in the Header
            for an authorized user""")
            def test_hpa_01_02_verify_auth_header_structure_and_visibility(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                structure_of_1st_level = page.get_structure_of_1st_level()
                visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_in_header()
                structure_of_2nd_level = page.get_structure_of_2nd_level()
                visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_in_header()
                structure_of_3rd_level = page.get_structure_of_3rd_level()
                visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_in_header()
                structure_of_4th_level = page.get_structure_of_4th_level()
                visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_in_header()
                structure_of_5th_level = page.get_structure_of_5th_level()
                visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_in_header()
                structure_of_6th_level = page.get_structure_of_6th_level()
                invisibility_of_elements_on_6th_level = page.check_elements_invisibility_on_6th_level_in_header()
                assert structure_of_1st_level, "The Header is empty"
                assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
                assert structure_of_2nd_level, "Elements on the 2nd level are absent in the Header"
                assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
                assert structure_of_3rd_level, "Elements on the 3rd level are absent in the Header"
                assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
                assert structure_of_4th_level, "Elements on the 4th level are absent in the Header"
                assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
                assert structure_of_5th_level, "Elements on the 5th level are absent in the Header"
                assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"
                assert structure_of_6th_level, "Elements on the 6th level are absent in the Header"
                assert invisibility_of_elements_on_6th_level, "6th-level elements are visible"

            @allure.title("Verify presence, visibility of links, buttons in the Header for an authorized user")
            def test_hpa_01_03_verify_auth_header_structural_elements(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                header_links = page.get_list_of_links_auth()
                header_direct_links = page.get_list_of_direct_links_auth()
                header_direct_links_visibility = page.check_direct_links_visibility_auth()
                links_in_more_presence = page.get_list_of_links_in_more()
                links_in_more_invisibility = page.check_links_invisibility_in_more()
                links_in_more_visibility = page.check_links_visibility_in_more()
                logo_link_presence = page.check_logo_link_presence()
                logo_link_visibility = page.check_logo_link_visibility()
                profile_link_presence = page.check_profile_link_presence()
                profile_link_visibility = page.check_profile_link_visibility()
                buttons_presence = page.get_list_of_buttons_auth()
                buttons_visibility = page.check_buttons_auth_visibility()
                ru_en_buttons_presence = page.get_list_of_ru_en_buttons()
                ru_en_buttons_visibility = page.check_ru_en_buttons_visibility()
                more_button_presence = page.check_more_button_presence()
                more_button_visibility = page.check_more_button_visibility()
                logout_button_presence = page.check_logout_button_presence()
                logout_button_visibility = page.check_logout_button_visibility()
                assert header_links, "Links are absent in the Header"
                assert header_direct_links, "Direct links are absent in the Header"
                assert header_direct_links_visibility, "Direct links are invisible"
                assert links_in_more_presence, "Links in the dropdown 'More' are absent in the Header"
                assert links_in_more_invisibility, "Links in the dropdown 'More' are visible"
                assert links_in_more_visibility, "Links in the dropdown 'More' are invisible"
                assert logo_link_presence, "The 'Logo' link is absent in the Header"
                assert logo_link_visibility, "The 'Logo' link is invisible"
                assert profile_link_presence, "The 'Profile' link is absent in the Header"
                assert profile_link_visibility, "The 'Profile' link is invisible"
                assert buttons_presence, "Buttons are absent in the Header"
                assert buttons_visibility, "Buttons are invisible"
                assert ru_en_buttons_presence, "The 'ru' and 'en' buttons are absent in the Header"
                assert ru_en_buttons_visibility, "The 'ru' and 'en' buttons are invisible"
                assert more_button_presence, "The 'More' button is absent in the Header"
                assert more_button_visibility, "The 'More' button is invisible"
                assert logout_button_presence, "The 'Logout' button is absent in the Header"
                assert logout_button_visibility, "The 'Logout' button is invisible"

        class TestAuHdPageText:
            @allure.title("Verify values of the text in links, buttons in the Header for an authorized user")
            def test_hpa_02_01_verify_auth_text_in_links_and_buttons(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                direct_links_text = page.get_text_in_direct_links_auth()
                links_in_more_text = page.get_text_of_links_in_more()
                buttons_text = page.get_text_in_buttons_auth()
                ru_en_buttons_text = page.get_text_in_ru_en_buttons()
                assert all(element in hPD.links_text_auth for element in direct_links_text[:4]), \
                    "Text in links in section 2 mismatches valid values"
                assert direct_links_text[4], "Text in the 'Profile' link is absent"
                assert all(element in hPD.links_text_auth for element in links_in_more_text), \
                    "Text in links in section 3 mismatches valid values"
                assert all(element in hPD.buttons_text for element in buttons_text), \
                    "Text in buttons mismatches valid values"
                assert all(element in hPD.ru_en_buttons_text for element in ru_en_buttons_text), \
                    "Text in 'ru-en' buttons mismatches valid values"

            @allure.title("Verify presence, visibility of the user name in the Header for an authorized user")
            def test_hpa_02_02_verify_auth_user_name(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                user_name_presence = page.check_user_name_presence()
                user_name_visibility = page.check_user_name_visibility()
                assert user_name_presence, "The user name is absent on the page"
                assert user_name_visibility, "The user name is invisible"

        class TestAuHdPageLinks:
            @allure.title("Verify clickability, href, status code of links in the Header for an authorized user")
            def test_hpa_03_01_verify_auth_header_links(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                links_clickability = page.check_links_clickability_auth()
                links_href = page.get_links_href_auth()
                link_status_codes = page.get_links_status_codes_auth()
                assert links_clickability, "Links are unclickable"
                assert links_href, "Links href are empty"
                assert all(element in hPD.set_auth for element in links_href), "Links href mismatch valid values"
                assert all(element in hPD.link_status_codes for element in link_status_codes), \
                    "Status codes of links mismatch valid values"

            @allure.title("""Verify if internal links in the Header for an authorized user 
            lead to correct pages after click""")
            def test_hpa_03_02_verify_auth_internal_links_lead_to_proper_pages(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                internal_links_in_more = page.get_list_of_internal_links_in_more()
                opened_pages = page.click_on_internal_links_in_header_auth()
                assert internal_links_in_more, "Internal links are not collected in the list"
                assert all(element in hPD.set_auth for element in opened_pages), \
                    "Some of internal links lead to incorrect pages after clicking"

            @allure.title("""Verify if external links in the Header for an authorized user 
            lead to correct pages after click""")
            def test_hpa_03_03_verify_auth_external_links_lead_to_proper_pages(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                external_links_in_more = page.get_list_of_external_links_in_more()
                opened_pages = page.click_on_external_links_in_header()
                assert external_links_in_more, "External links are not collected in the list"
                assert all(element in hPD.set_auth for element in opened_pages), \
                    "Some of external links lead to incorrect pages after clicking"

            @allure.title("""Verify that the Logo link on the Start Authorized Page 
                             doesn't refresh the current page or lead to other pages after clicking""")
            def test_hpa_03_04_verify_click_auth_logo_link(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                handles_before = driver.window_handles
                initial_page_source = page.driver.page_source
                initial_page_url = page.driver.current_url
                current_page_url = page.click_on_logo_link()
                handles_after = driver.window_handles
                current_page_source = page.driver.page_source
                assert len(handles_before) == len(handles_after), "The number of open tabs changed after clicking"
                assert initial_page_source == current_page_source, \
                    "Logo link in the Header refreshes the page after clicking"
                assert initial_page_url == current_page_url, "Logo link in the Header leads to some page after clicking"

            @allure.title("""Verify the dropdown opens/closes after clicking on the 'More' button in the Header 
               for an authorized user""")
            def test_hpa_03_05_verify_auth_more_button_click(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                button_click = page.check_dropdown_opens_and_closes()
                assert button_click, "The dropdown isn't open/closed after clicking the 'More' button"

            @allure.title("Verify switching of the 'ru', 'en' buttons in the Header for an authorized user")
            def test_hpa_03_06_verify_auth_ru_en_buttons_switching(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                text_ru = page.check_language_change_ru_auth()
                text_en = page.check_language_change_en_auth()
                assert text_ru == hPD.title_text_ru_auth, "RU language isn't enabled after clicking the 'ru' button"
                assert text_en == hPD.title_text_en_auth, "EN language isn't enabled after clicking the 'en' button"

            @allure.title("Verify user logout after clicking the 'Logout' button in the Header for an authorized user")
            def test_hpa_03_07_verify_auth_user_logout_by_logout_button_click(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                button_click = page.check_auth_user_logout()
                assert button_click in hPD.titles_text_unauth, "A user is authorized after clicking the Logout button"

        class TestAuHdPageImages:
            @allure.title("""Verify presence, visibility and attributes of the image in the Logo link in the Header 
               for an authorized user""")
            def test_hpa_04_01_verify_auth_logo_image(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                logo_image_presence = page.check_auth_logo_image_presence()
                logo_image_visibility = page.check_auth_logo_image_visibility()
                image_xmlns = page.get_xmlns_of_auth_logo_image()
                assert logo_image_presence, "An image in the Logo link is absent on the page"
                assert logo_image_visibility, "The Logo image is invisible"
                assert image_xmlns, "The 'xmlns' attribute value of the Logo image is empty"
                assert image_xmlns == hPD.logo_image_xmlns, \
                    "The xmlns attribute of the Logo image mismatches valid value"

            @allure.title("Verify size of the image in the 'Logo' link in the Header for an authorized user")
            def test_hpa_04_02_verify_auth_logo_image_size(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                image_size = page.get_size_of_auth_logo_image()
                image_size_change = page.check_size_changes_of_auth_logo_image()
                assert image_size != 0, f"The image in the 'Logo' image has not size"
                assert image_size_change, "The 'Logo' image size is changed"

            @allure.title("Verify presence, visibility, attributes of icons in the Header for an authorized user")
            def test_hpa_04_03_verify_auth_icons(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                icons_presence = page.get_list_of_auth_icons()
                icons_visibility = page.check_auth_icons_visibility()
                icons_xmlns = page.get_auth_icons_xmlns()
                assert icons_presence, "Icons in the Header are absent"
                assert icons_visibility, "Icons in the Header are invisible"
                assert icons_xmlns, "The 'xmlns' attribute value of icons in the Header are empty"
                assert all(element in hPD.icons_xmlns for element in icons_xmlns), \
                    "The 'xmlns' attribute value of some icons is empty or invalid"

            @allure.title("""Verify presence, visibility and attributes of the profile avatar in the Header 
               for an authorized user""")
            def test_hpa_04_04_verify_auth_profile_avatar(self, driver, auto_test_user_authorized):
                page = hPage(driver)
                profile_avatar_presence = page.check_auth_profile_avatar_presence()
                profile_avatar_visibility = page.check_auth_profile_avatar_visibility()
                profile_avatar_src = page.get_src_of_auth_profile_avatar()
                profile_avatar_alt = page.get_alt_of_auth_profile_avatar()
                assert profile_avatar_presence, "The profile avatar is absent on the page"
                assert profile_avatar_visibility, "The profile avatar is invisible"
                assert profile_avatar_src, "The 'src' attribute value of the profile avatar is empty"
                assert profile_avatar_src == hPD.profile_avatar_src, \
                    "The 'src' attribute value of the profile avatar mismatches the valid value"
                assert profile_avatar_alt, "The 'alt' attribute value of the profile avatar is empty"
                assert profile_avatar_alt == hPD.profile_avatar_alt, \
                    "The 'alt' attribute value of the profile avatar mismatches the valid value"
