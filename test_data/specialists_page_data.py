"""Data for verifying web elements on the 'Specialists' page"""
from test_data.links import MainPageLinks as Links


class SpecialistsPageData:
    tab_title = ("Специалисты | BrainUp", "Specialists | BrainUp")

    page_title = ("Специалисты", "Specialists")

    text_on_page = ("Обучающая программа BrainUp разработана совместно с лучшими специалистами "
                    "в области сурдопедагогики из России и Беларуси",
                    "The BrainUp training program was developed jointly with the best specialists "
                    "in the field of deaf education from Russia and Belarus")

    spec_names = ("Гарбарук Екатерина Сергеевна", "Прошина Любовь Александровна", "Березкина Ксения Сергеевна",
                         "Метельская Наталья Николаевна", "Королева Инна Васильевна", "Юлия Кибалова",
                         "Платоненко Дарья Сергеевна", "Сивенкова Кристина Александровна",
                         "Ekaterina Garbaruk", "Lubov Proshina", "Ksenia Berezkina", "Natalia Metelskaya",
                         "Inna Koroleva", "Yulia Kibalova", "Daria Platonenko", "Kristina Sivenkova")

    spec_professions = (
        "Кандидат биологических наук, специалист Лаборатории слуха и речи ПСПбГМУ, специалист "
         "в области диагностики слуховых нарушений",
         "Сурдопедагог, РНПЦ оториноларингологии, опыт работы более 10 лет",
         "Сурдопедагог, Городской ресурсный центр для детей с нарушением слуха, опыт работы более 10 лет",
         "Сурдопедагог, УЗ Могилевская областная детская больница, опыт работы более 20 лет",
         'Научный руководитель реабилитационного отделения, доктор психологических наук, профессор, '
         'автор серии методических пособий "Учусь слушать и говорить"',
         "Сурдопедагог, дефектолог, Лаборатория слуха и речи ПСПбГМУ, опыт работы более 10 лет",
         "Сурдопедагог, РНПЦ оториноларингологии, опыт работы более 3 лет",
         "Сурдопедагог, СПб Сурдоцентр, молодой специалист",
        "Candidate of Biological Sciences, expert at the Laboratory of Hearing and Speech "
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
         "Teacher of the deaf, Saint Petersburg Center of Otorhinolaryngology, young professional")

    all_spec_link_text = ("Все Специалисты", "All Specialists")

    all_spec_link_href = f"{Links.URL_MAIN_PAGE}specialists#"

    all_spec_link_status_code = (200,)

    s = 'https://brnup.s3.eu-north-1.amazonaws.com/pictures/specialists/'
    e = '.png'
    images_src = (f'{s}garbaruk{e}', f'{s}proshina{e}', f'{s}berezkina{e}', f'{s}metelskaya{e}',
                  f'{s}koroleva{e}', f'{s}kibalova{e}', f'{s}platonenko{e}', f'{s}sivenkova{e}')

    images_alt = "user avatar"

    page_url = f"{Links.URL_MAIN_PAGE}specialists"
