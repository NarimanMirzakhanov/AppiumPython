from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class FlightsScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_flights(self, flight_from, destination):
        self.click("flightfrom_ID")
        self.type("search_ID", flight_from)
        self.click_index("selectfrom_XPATH", 2)
        self.click("destination_ID")
        self.type("search_ID", destination)
        self.click_index("selectfrom_XPATH", 2)
        self.click("search_XPATH")
        self.click("gotitbtn_ID")
