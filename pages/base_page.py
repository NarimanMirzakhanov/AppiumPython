import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from utilities import config_reader
from utilities.log_util import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, (config_reader.read_config("locators", locator))).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, (config_reader.read_config("locators", locator))).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, (config_reader.read_config("locators", locator))).click()
        log.logger.info("Clicking on an Element " + str(locator))

    def click_index(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_elements(AppiumBy.XPATH, (config_reader.read_config("locators", locator)))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, (config_reader.read_config("locators", locator)))[
                index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(AppiumBy.ID, (config_reader.read_config("locators", locator)))[index].click()
        log.logger.info("Clicking on an Element " + str(locator) + " with index: " + str(index))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, (config_reader.read_config("locators", locator))).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                     (config_reader.read_config("locators", locator))).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, (config_reader.read_config("locators", locator))).send_keys(value)
        log.logger.info("Typing in an Element " + str(locator) + " entered the value as: " + str(value))

    def get_text(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(AppiumBy.XPATH, (config_reader.read_config("locators", locator))).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                            (config_reader.read_config("locators", locator))).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(AppiumBy.ID, (config_reader.read_config("locators", locator))).text
        log.logger.info("Getting text from an Element " + str(locator))
        return text
