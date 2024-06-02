"""Data for verifying web elements in the Header on web pages"""


class HeaderData:

    links_href = {
        "logo_link_href": "https://brainup.site/",
        "section 2 links href": ["https://brainup.site/description", "https://t.me/BrainUpUsers"]
    }

    links_status_code = 200

    links_text = [
        ["ОПИСАНИЕ", "TELEGRAM"], ["ABOUT", "TELEGRAM"]
    ]

    logo_image_xmlns = "http://www.w3.org/2000/svg"

    pages_url_for_navigation_by_links_in_section_2 = [
        "https://brainup.site/description",
        "https://brainup.site/",
        "https://t.me/BrainUpUsers",
        "https://brainup.site/"
    ]
