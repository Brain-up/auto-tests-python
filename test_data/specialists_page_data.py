"""Data for verifying web elements on the 'Specialists' page"""


class SpecialistsPageData:
    specialists_page_elements_content = {
        "page_text_content": ["Обучающая программа BrainUp разработана совместно с лучшими специалистами "
                              "в области сурдопедагогики из России и Беларуси",
                              "The BrainUp training program was developed jointly with the best specialists "
                              "in the field of deaf education from Russia and Belarus"],
        "page_title_content": ["Специалисты", "Specialists"]
    }

    specialists_page_grid_size = 8

    specialists_page_images_src = {
        "1th_card_img_src": "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/garbaruk.png"
    }

    specialists_images_alt = "user avatar"

    specialists_images_src = [
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/garbaruk.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/proshina.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/berezkina.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/metelskaya.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/koroleva.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/kibalova.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/platonenko.png",
        "https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/sivenkova.png"
    ]

    specialists_names = [
        ["Гарбарук Екатерина Сергеевна", "Прошина Любовь Александровна", "Березкина Ксения Сергеевна",
         "Метельская Наталья Николаевна", "Королева Инна Васильевна", "Юлия Кибалова", "Платоненко Дарья Сергеевна",
         "Сивенкова Кристина Александровна"],
        ["Ekaterina Garbaruk", "Lubov Proshina", "Ksenia Berezkina", "Natalia Metelskaya", "Inna Koroleva",
        "Yulia Kibalova", "Daria Platonenko", "Kristina Sivenkova"]
    ]

    specialists_professions = [
        ["Кандидат биологических наук, специалист Лаборатории слуха и речи ПСПбГМУ, специалист "
         "в области диагностики слуховых нарушений",
         "Сурдопедагог, РНПЦ оториноларингологии, опыт работы более 10 лет",
         "Сурдопедагог, Городской ресурсный центр для детей с нарушением слуха, опыт работы более 10 лет",
         "Сурдопедагог, УЗ Могилевская областная детская больница, опыт работы более 20 лет",
         'Научный руководитель реабилитационного отделения, доктор психологических наук, профессор, '
         'автор серии методических пособий "Учусь слушать и говорить"',
         "Сурдопедагог, дефектолог, Лаборатория слуха и речи ПСПбГМУ, опыт работы более 10 лет",
         "Сурдопедагог, РНПЦ оториноларингологии, опыт работы более 3 лет",
         "Сурдопедагог, СПб Сурдоцентр, молодой специалист"],
        ["Candidate of Biological Sciences, expert at the Laboratory of Hearing and Speech "
         "(The Pavlov First Saint Petersburg State Medical University), expert in diagnosis of aural disorders",
         "Teacher of the deaf, Belarusian Republican Scientific and Practical Center of Otorhinolaryngology, "
         "10+ years of experience",
         "Teacher of the deaf, City Resource Center for Hearing Impaired Children, 10+ years of experience",
         "Teacher of the deaf, Mogilev Regional Children's Hospital (Belarus), 20+ years of experience",
         'Academic supervisor of the rehabilitation department, Doctor of Psychology, Professor, '
         'author of the manuals "Learning to listen and speak"',
         "Teacher of the deaf, defectologist, expert at the Laboratory of Hearing and Speech "
         "(The Pavlov First Saint Petersburg State Medical University), 10+ years of experience",
         "Teacher of the deaf, Belarusian Republican Scientific and Practical Center of Otorhinolaryngology, "
         "3+ years of experience",
         "Teacher of the deaf, Saint Petersburg Center of Otorhinolaryngology, young professional"]
    ]

    all_specialists_link_href = "https://brainup.site/specialists#"

    all_specialists_link_status_code = 200

    all_specialists_link_text = ["Все Специалисты", "All Specialists"]
