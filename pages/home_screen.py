import time

from pages.base_page import BasePage
from pages.bus_screen import BusScreen
from pages.flights_screen import FlightsScreen
from pages.hotel_screen import HotelScreen
from pages.train_screen import TrainScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_hotels(self):
        time.sleep(3)

        self.click("hotels_XPATH")
        time.sleep(5)
        return HotelScreen(self.driver)

    def go_to_flights(self):
        self.click("flights_XPATH")
        return FlightsScreen(self.driver)


    def go_to_trains(self):
        self.click("trains_XPATH")
        return TrainScreen(self.driver)

    def go_to_bus(self):
        self.click("bus_XPATH")
        return BusScreen(self.driver)
