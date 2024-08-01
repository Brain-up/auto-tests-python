"""Data for verifying web elements in the Footer"""


class FooterData:
    with_the_support_text = ["При поддержке", "With the support"]
    contact_us_link_text = ["Обратная связь", "Contact us"]

    footer_images_src = {
        "arasaac_img_src": "https://brainup.site/logos/logo_ARASAAC_black-6aced95542b919137b28bced5be83596.png",
        "epam_img_src": "https://brainup.site/logos/epam-cd401151c8ee5f14afbba10b72cd5fea.png",
        "jetbrains_img_src": "https://brainup.site/logos/jetbrains-variant-4_-fb6c06f46c4a6267ac60e84343940d8b.png",
        "reg_img_src": "https://brainup.site/logos/reg-ru.svg",
        "selectel_img_src": "https://brainup.site/logos/selectel-f49f7fdb2061466c4f28aa1e128bd9a4.png"
    }

    footer_images_alt = {
        "arasaac_img_alt": "ARASAAC",
        "epam_img_alt": "EPAM",
        "jetbrains_img_alt": "JetBrains",
        "reg_img_alt": "Регистратор доменных имен РЕГ.РУ",
        "selectel_img_alt": "Selectel"
    }

    footer_links_href = {
        "arasaac_link_href": "https://arasaac.org/",
        "contact_us_link_href": "mailto:brainupproject@yandex.ru?subject=BrainUp",
        "epam_link_href": "https://epam.com/",
        "jetbrains_link_href": "https://www.jetbrains.com/",
        "reg_link_href": "https://reg.ru/",
        "selectel_link_href": "https://selectel.ru/"
    }

    footer_links_status_codes = {
        "arasaac_link_status_code": 200,
        "epam_link_status_code": 301,
        "jetbrains_link_status_code": 200,
        "reg_link_status_code": [200, 301, 302],
        "selectel_link_status_code": 200
    }

    # Related web pages elements text
    footer_related_elements_text = {
        "arasaac_start_page_text": ["Центр альтернативной и аументативной коммуникации Арагона",
                                    "Aragonese Center of Augmentative and Alternative Communication"],
        "epam_start_page_text": "We can help you",
        "jetbrains_start_page_text": "The complete\ndeveloper toolkit",
        "reg_start_page_text": "Вход",
        "selectel_start_page_text": "Продукты и предложения"
    }
