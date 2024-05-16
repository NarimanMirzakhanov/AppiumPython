import time

from pages.base_page import BasePage


class HotelScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_hotel(self, city):
        self.click("destination_XPATH")
        self.type("searchtext_XPATH", city)
        time.sleep(2)
        self.click_index("selectlocation_XPATH", 2)
        self.click("closepopup_ID")
        # self.click("searchbtn_XPATH")
