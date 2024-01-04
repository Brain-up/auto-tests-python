import os


class Data:

    DEFAULT_USER_1 = {'login': 'autoTestSpecialist@brainup.spb.ru',
                      'password': 'password'}  # default user with limited access
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    DEFAULT_USER_2 = {'login': 'default@default.ru', 'password': 'password'}  # default user with limited access


class FooterData:
    footer_elements_text = {
        "CONTACT_US_LINK": ["Обратная связь", "Contact us"],
        "WITH_THE_SUPPORT_PHRASE": ["При поддержке", "With the support"]
    }

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
