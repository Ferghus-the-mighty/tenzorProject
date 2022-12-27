import time
from webpages.YandexPages import SearchHelper, YandexLocators


def test_yandex_search(browser):
    ya = SearchHelper(browser)
    ya.go_to_site()
    assert ya.check_element_exists(YandexLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    ya.enter_word("Тензор")
    assert ya.check_element_exists(YandexLocators.LOCATOR_YANDEX_SUGGEST_FIELD)

    ya.click_enter()
    assert ya.check_link('https://tensor.ru/')


def test_yandex_pictures(browser):
    ya = SearchHelper(browser)
    ya.go_to_site()
    assert ya.check_element_exists(YandexLocators.LOCATOR_ADD_SERVICES)

    ya.click_element(YandexLocators.LOCATOR_ADD_SERVICES)
    assert ya.check_element_exists(YandexLocators.LOCATOR_IMAGES_BUTTON)

    ya.click_element(YandexLocators.LOCATOR_IMAGES_BUTTON)
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://yandex.ru/images/'

    first_category_name = ya.get_attribute(YandexLocators.LOCATOR_FIRST_CATEGORY, 'data-grid-text')
    ya.click_element(YandexLocators.LOCATOR_FIRST_CATEGORY)
    input_text = ya.get_attribute(YandexLocators.LOCATOR_IMAGES_INPUT, 'value')
    assert first_category_name == input_text

    ya.click_element(YandexLocators.LOCATOR_FIRST_IMAGE)
    assert ya.check_element_exists(YandexLocators.LOCATOR_IMAGE_OPENED)
    time.sleep(2)

    first_image = ya.get_attribute(YandexLocators.LOCATOR_IMAGE_OPENED, 'src')
    ya.click_element(YandexLocators.LOCATOR_BUTTON_RIGHT)
    time.sleep(2)
    second_image = ya.get_attribute(YandexLocators.LOCATOR_IMAGE_OPENED, 'src')
    assert first_image != second_image
    time.sleep(2)

    ya.click_element(YandexLocators.LOCATOR_BUTTON_LEFT)
    first_image_again = ya.get_attribute(YandexLocators.LOCATOR_IMAGE_OPENED, 'src')
    assert first_image == first_image_again
