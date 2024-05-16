import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from pages.home_screen import HomeScreen
from test_cases.base_test import BaseTest
from utilities import data_provider
from utilities.scroll_util import ScrollUtil


class TestSearchFlights(BaseTest):

    @pytest.mark.parametrize("flight_from, destination", data_provider.get_data("SearchFlights"))
    def test_search_hotel(self, flight_from, destination):
        home = HomeScreen(self.driver)
        home.go_to_flights().search_flights(flight_from, destination)
        time.sleep(3)
        ScrollUtil.scroll_to_text_by_android_UI_automator("Emirates", self.driver)
        # ScrollUtil.swipe_up(3, self.driver)




