from typing import Tuple

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)
        self.__action = ActionChains(self._driver)


    def _wait_until_element_appears(self, locator: Tuple[By, str]) -> WebElement:
        return self.__web_driver_wait.until(
            EC.presence_of_element_located(locator)
        )

    def _click(self, locator: Tuple[By, str]) -> WebElement:
        self._wait_until_element_appears(locator).click()


    def _scroll_page(self, locator: Tuple[By, str]) -> WebElement:
        selector = self._wait_until_element_appears(locator)
        self.__action.move_to_element(selector).perform()

    def _input_field(self, locator: Tuple[By, str], text: str) -> WebElement:
        selector = self._wait_until_element_appears(locator)
        selector.send_keys(text)


    def _is_displayed(self, locator: Tuple[By, str]) -> WebElement:
        selector = self._wait_until_element_appears(locator)
        selector.is_displayed()

