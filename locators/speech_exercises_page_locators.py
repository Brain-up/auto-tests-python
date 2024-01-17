import random

from selenium.webdriver.common.by import By


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """
    BUTTON_INTERACT = (By.XPATH, '//*[text()="Interact"]')
    BUTTON_SOLVE = (By.XPATH, '//*[text()="Solve"]')
    BUTTON_START = (By.XPATH, '//button[@aria-label="Start exercise"]')
    LIST_WORDS_IN_CARD = (By.XPATH, '//li[@class="task-player__option flex"]')
    PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar"]')

    # Language
    FAMILY_CARD_RU = (By.XPATH, '//a[@title="Слова про семью"]')
    FAMILY_CARD_EN = (By.XPATH, '//a[@title="Family words"]')

    # SubGroups
    SENTENCES = (By.ID, 'ember315')
    SIMILAR_PHRASES = (By.ID, 'ember313')
    SIMILAR_PHRASES_GROUP = (By.XPATH, '(//aside//li)[1]')
    WORDS = (By.XPATH, '//button[@data-test-active-link="Words"]')
    WORDS_GROUP = (By.ID, 'ember314')
    WORDS_GROUP_BY_FREQUENCY = (By.ID, 'ember316')

    # WORDS
    LIST_OF_CARD_FROM_WORDS = (
        By.XPATH,
        '//div[@class="sm:tracking-normal sm:leading-normal sm:text-base '
        'text-xs leading-none tracking-tighter text-center"]')

    RANDOM_CARD_FROM_WORDS = (By.XPATH,
                              f'//div[@class="sm:tracking-normal sm:leading-normal '
                              f'sm:text-base text-xs leading-none tracking-tighter text-center"]'
                              f'[{str(random.randint(1, len(LIST_OF_CARD_FROM_WORDS)))}]')

    LIST_CARDS_ID = (By.XPATH, '//div[@class="flex"]')
    RANDOM_CARDS_FROM_SIMILAR = (By.XPATH, f'//div[@class="flex"][{str(random.randint(1, len(LIST_CARDS_ID)))}]')

    # Cards in the SIMILAR PHRASES GROUP
    CARDS_LIST_IN_SIMILAR_PHRASES = (By.XPATH, '//div[contains(@class, "series-container")]//a')
