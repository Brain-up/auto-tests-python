import random

from selenium.webdriver.common.by import By


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """
    BUTTON_START = (By.XPATH, '//button[@aria-label="Start exercise"]')
    LIST_WORDS_IN_CARD = (By.XPATH, '//li[@class="task-player__option flex"]')
    PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar"]')
    BUTTON_SOLVE = (By.XPATH, '//*[text()="Solve"]')
    BUTTON_INTERACT = (By.XPATH, '//*[text()="Interact"]')

    # Language
    FAMILY_CARD_RU = (By.XPATH, '//a[@title="Слова про семью"]')
    FAMILY_CARD_EN = (By.XPATH, '//a[@title="Family words"]')

    # SubGroups
    SIMILAR_PHRASES = (By.ID, 'ember313')
    WORDS_GROUP = (By.ID, 'ember314')
    SENTENCES = (By.ID, 'ember315')
    WORDS_GROUP_BY_FREQUENCY = (By.ID, 'ember316')
    WORDS = (By.XPATH, '//button[@data-test-active-link="Words"]')

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
