from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException


# BasePage is a class that contains all the common methods that are used in all the pages
# of the application. This class is inherited by all the page objects.
class BasePage:
    # The constructor of the class receives the driver as a parameter.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Private methods

    # The _open_url method is used to open a URL in the browser.
    def _open_url(self, url: str):
        self.driver.get(url)

    # The _find method is used to find an element in the page.
    def _find(self, locator: tuple) -> WebElement:
        # The * operator is used to unpack the tuple and pass the two parameters to the find_element method.
        return self.driver.find_element(*locator)

    # The _wait_for_element method is used to wait for an element to be visible in the page.
    def _wait_for_element(self, locator: tuple, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    # The _get_text method is used to get the text of an element.
    def _get_text(self, locator: tuple, timeout: int = 10) -> str:
        self._wait_for_element(locator, timeout)
        return self._find(locator).text

    # The _type method is used to type text in a text field.
    def _type(self, locator: tuple, text: str, timeout: int = 10):
        self._wait_for_element(locator, timeout)
        self._find(locator).clear()
        self._find(locator).send_keys(text)

    # The _click method is used to click on a button.
    def _click(self, locator: tuple, timeout: int = 10):
        self._wait_for_element(locator, timeout)
        self._find(locator).click()

    # The _is_displayed method is used to check if an element is displayed in the page.
    def _is_displayed(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            self._wait_for_element(locator, timeout)
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
