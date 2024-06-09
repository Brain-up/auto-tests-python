"""Data for verifying web elements on the 'Used Resources' page and related pages"""


class UsedResourcesPageData:
    tab_title_current = "Brn"
    tab_title_expected = ["Используемые ресурсы | BrainUp", "Used Resources | BrainUp"]

    title_h1 = ["Используемые ресурсы", "Used Resources"]

    used_resources_page_elements_content = {
        "page_text_content": ["Фотографии упражнений в приложении взяты со следующих платформ:",
                              "Exercise pictures in the application are taken from the following platforms:"],
        "flora_link_content": "Flora («Flora von Deutschland, Österreich und der Schweiz in Wort und Bild für "
                              "Schule und Haus»)",
        "freepik_com_link_content": "freepik.com",
        "plants_link_content": "Plants (Köhler's Medizinal-Pflanzen)"
    }

    links_href = ["https://freepik.com/",
                  "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_"
                  "%D1%80%D0%B0%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%B9,"
                  "_%D0%B8%D0%BB%D0%BB%D1%8E%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8_%D0%BA_"
                  "%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%BC_"
                  "%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D1%8B_%D0%B2_"
                  "%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B5_"
                  "K%C3%B6hler%E2%80%99s_Medizinal-Pflanzen",
                  "https://web.archive.org/web/20090601012031/http://caliban.mpiz-koeln.mpg.de/~stueber/"
                  "thome/Alphabetical_list.html"
                  ]

    links_status_codes = [200, 301]

    # Related web pages titles
    pages_titles = [
        "Список растений, иллюстрации к которым размещены в справочнике Köhler’s Medizinal-Pflanzen — Википедия",
        "List of plants whose illustrations are included in the Köhler's Medizinal-Pflanzen reference book - Wikipedia",
        "Freepik | Create great designs, faster",
        "Thomé - Flora von Deutschland Österreich und der Schweiz"
    ]

    icons_xmlns = "http://www.w3.org/2000/svg"
