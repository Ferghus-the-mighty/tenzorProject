from webpages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class YandexLocators:
    """Yandex Search locators"""
    LOCATOR_YANDEX_SEARCH_FIELD = (By.XPATH, "//input[@class='search3__input mini-suggest__input']")
    LOCATOR_YANDEX_SUGGEST_FIELD = (By.CLASS_NAME, 'mini-suggest__popup-container')
    LOCATOR_RESULT_LINKS = (By.XPATH,
                            "//a[@class='Link Link_theme_outer Path-Item link path__item link organic__greenurl']")
    LOCATOR_ADD_SERVICES = (By.CLASS_NAME, 'services-pinned__content')
    LOCATOR_IMAGES_BUTTON = (By.XPATH, "//div[@class='services-pinned__more-popup-item-title' and text()='Картинки']")
    LOCATOR_FIRST_CATEGORY = (By.XPATH, "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']")
    LOCATOR_IMAGES_INPUT = (By.XPATH, "//input[@class='input__control mini-suggest__input']")
    LOCATOR_FIRST_IMAGE = (By.XPATH,
                           "//div[@class='serp-item serp-item_type_search serp-item_group_search serp-item_pos_0 "
                           "justifier__item i-bem justifier__item_first']")
    LOCATOR_IMAGE_OPENED = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_BUTTON_RIGHT = (By.CSS_SELECTOR,
                            '.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button')
    LOCATOR_BUTTON_LEFT = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button')


class SearchHelper(BasePage):

    def check_element_exists(self, locator):
        """Check if element exists on page"""
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def enter_word(self, word):
        """Enter word into field"""
        search_field = self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_enter(self):
        """Imitate Enter button click"""
        search_field = self.find_element(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)
        return search_field

    def check_link(self, link):
        """Compare first link from searching results with given link"""
        result_links = self.find_elements(YandexLocators.LOCATOR_RESULT_LINKS)
        link_expected = result_links[0].get_attribute('href')
        return link_expected == link

    def click_element(self, locator):
        """Imitate left mouse button click"""
        element = self.find_element(locator)
        element.click()
        return element

    def get_attribute(self, locator, attribute):
        """Get attribute of element"""
        element = self.find_element(locator)
        text = element.get_attribute(attribute)
        return text
