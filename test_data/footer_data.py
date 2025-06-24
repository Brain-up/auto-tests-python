"""Data for verifying web elements in the Footer"""
from test_data.links import MainPageLinks as Links


class FooterData:
    with_the_support_text = ("При поддержке", "With the support")
    contact_us_link_text = ("Обратная связь", "Contact us")

    link_titles = ("brainupproject@yandex.ru",)

    link1 = "https://arasaac.org/"
    link2 = "mailto:brainupproject@yandex.ru?subject=BrainUp"
    link3 = "https://epam.com/"
    link4 = "https://www.jetbrains.com/"
    link5 = "https://reg.ru/"
    link6 = "https://selectel.ru/"

    links_href = (link1, link2, link3, link4, link5, link6)

    link_status_codes = (200, 403)

    s = f"{Links.URL_MAIN_PAGE}logos/"
    images_src = (f"{s}logo_ARASAAC_black-6aced95542b919137b28bced5be83596.png",
                  f"{s}epam-cd401151c8ee5f14afbba10b72cd5fea.png",
                  f"{s}jetbrains-variant-4_-fb6c06f46c4a6267ac60e84343940d8b.png",
                  f"{s}reg-ru.svg",
                  f"{s}selectel-f49f7fdb2061466c4f28aa1e128bd9a4.png")

    images_alt = ("ARASAAC", "EPAM", "JetBrains", "Регистратор доменных имен РЕГ.РУ", "Selectel")

    # Related web pages urls
    domains = ['arasaac.org', 'epam.com', 'jetbrains.com', 'reg.ru', 'selectel.ru']  # the list of domains
