"""Data for verifying web elements in the Header on web pages"""


class HeaderData:
    links_text = [
        ["ОПИСАНИЕ", "TELEGRAM"], ["ABOUT", "TELEGRAM"]
    ]

    links_href = [
        "https://brainup.site/",
        "https://brainup.site/description",
        "https://t.me/BrainUpUsers",
        "https://opencollective.com/brainup",
        "https://github.com/Brain-up/brn",
        "https://brainup.site/contact",
        "https://brainup.site/specialists",
        "https://brainup.site/contributors",
        "https://brainup.site/used-resources",
        "https://brainup.site/registration"
    ]

    link_status_codes = 200

    logo_image_xmlns = "http://www.w3.org/2000/svg"

    pages_url_for_navigation_by_links_in_section_2 = [
        "https://brainup.site/description",
        "https://brainup.site/",
        "https://t.me/BrainUpUsers",
        "https://brainup.site/"
    ]
