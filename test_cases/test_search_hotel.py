import pytest

from pages.home_screen import HomeScreen
from pages.hotel_screen import HotelScreen
from test_cases.base_test import BaseTest
from utilities import data_provider


class TestSearchHotel(BaseTest):

    @pytest.mark.parametrize("city", data_provider.get_data("SearchTest"))
    def test_search_hotel(self, city):
        home = HomeScreen(self.driver)
        home.go_to_hotels().search_hotel(city)


