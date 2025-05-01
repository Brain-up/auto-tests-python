"""Data for verifying web elements in the Footer"""
from test_data.links import MainPageLinks as Links


class FooterData:
    with_the_support_text = ("При поддержке", "With the support")
    contact_us_link_text = ("Обратная связь", "Contact us")

    link_titles = "brainupproject@yandex.ru"

    links_href = ("https://arasaac.org/",
                  "mailto:brainupproject@yandex.ru?subject=BrainUp",
                  "https://epam.com/",
                  "https://www.jetbrains.com/",
                  "https://reg.ru/",
                  "https://selectel.ru/")

    link_status_codes = (200, 403)

    images_src = (f"{Links.URL_MAIN_PAGE}logos/logo_ARASAAC_black-6aced95542b919137b28bced5be83596.png",
                  f"{Links.URL_MAIN_PAGE}logos/epam-cd401151c8ee5f14afbba10b72cd5fea.png",
                  f"{Links.URL_MAIN_PAGE}logos/jetbrains-variant-4_-fb6c06f46c4a6267ac60e84343940d8b.png",
                  f"{Links.URL_MAIN_PAGE}logos/reg-ru.svg",
                  f"{Links.URL_MAIN_PAGE}logos/selectel-f49f7fdb2061466c4f28aa1e128bd9a4.png")

    images_alt = ("ARASAAC", "EPAM", "JetBrains", "Регистратор доменных имен РЕГ.РУ", "Selectel")

    # Related web pages urls
    pages_urls = ("https://arasaac.org/",
                  "https://www.epam.com/", "https://epam.com/",
                  "https://www.jetbrains.com/",
                  "https://www.reg.ru/", "https://reg.ru/",
                  "https://www.reg.ru/?utm_source=brainup.site&utm_medium=referral&utm_campaign=brainup.site&utm_referrer=brainup.site",
                  "https://selectel.ru/")
