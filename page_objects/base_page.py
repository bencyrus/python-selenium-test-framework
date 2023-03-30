from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def _wait_for_element(self, locator: tuple, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, timeout: int = 10):
        self._wait_for_element(locator, timeout)
        self._find(locator).clear()
        self._find(locator).send_keys(text)
    
    def _click(self, locator: tuple, timeout: int = 10):
        self._wait_for_element(locator, timeout)
        self._find(locator).click()
    
    def _is_displayed(self, locator: tuple, timeout: int = 10):
        try:
            self._wait_for_element(locator, timeout)
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False