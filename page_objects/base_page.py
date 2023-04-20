import logging
from datetime import datetime
from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    # BasePage is a class that contains all the common methods that are used in all the pages
    # of the application. This class is inherited by all the page objects.

    def __init__(self, driver):
        self.driver = driver
        self.logger = self._create_logger()

    def _create_logger(self) -> logging.Logger:
        # Creates a logger instance and configures it.
        # The log file name is based on the current date and time.
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            log_file_name = datetime.now().strftime("logs/logfile_%Y_%m_%d_%H_%M_%S.txt")
            file_handler = logging.FileHandler(log_file_name)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    def _open_url(self, url: str) -> None:
        # Opens a URL in the browser.
        self.driver.get(url)

    def _get_current_url(self) -> str:
        # Returns the current URL.
        return self.driver.current_url

    def _find_element(self, locator: tuple) -> WebElement:
        # Finds an element in the page.
        return self.driver.find_element(*locator)

    def _wait_for_visible_element(self, locator: tuple, timeout: int = 10) -> None:
        # Waits for an element to be visible in the page.
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def _get_text(self, locator: tuple, timeout: int = 10) -> str:
        # Gets the text of an element.
        self._wait_for_visible_element(locator, timeout)
        return self._find_element(locator).text

    def _type(self, locator: tuple, text: str, timeout: int = 10) -> None:
        # Types text in a text field.
        self._wait_for_visible_element(locator, timeout)
        element = self._find_element(locator)
        self._scroll_to_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def _click(self, locator: tuple, timeout: int = 10) -> None:
        # Clicks on a button.
        self._wait_for_visible_element(locator, timeout)
        self._scroll_to_element(locator, timeout)
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def _is_displayed(self, locator: tuple, timeout: int = 10) -> bool:
        # Checks if an element is displayed in the page.
        try:
            self._wait_for_visible_element(locator, timeout)
            return self._find_element(locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def _scroll_to_element(self, locator: tuple, timeout: int = 10) -> None:
        # Scrolls to an element.
        self._wait_for_visible_element(locator, timeout)
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _go_back(self) -> None:
        # Goes back to the previous page.
        self.driver.back()

    def _log(self, message: str) -> None:
        # Logs a given message using the logger instance.
        self.logger.info(message)
