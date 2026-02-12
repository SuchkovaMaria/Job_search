from unittest.mock import patch

import pytest

from src.aircraft_info_class import AirplaneInfo
from src.class_request_api import Aircraft
from src.utils import filter_aeroplanes, get_aeroplanes_by_altitude, sorted_aircraft_height


def test_ranged_aeroplanes():
    with pytest.raises(ValueError):
        assert get_aeroplanes_by_altitude([], "1")


@patch("requests.get")
def test_get_aeroplanes_by_altitude(mock_requests, coord, list_aircraft_1, dict_1):
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.side_effect = [coord, dict_1, list_aircraft_1]

    aircraft = Aircraft()
    aircraft.get_coordinates("canada")
    airplane_list = AirplaneInfo.list_aircraft(aircraft)
    filtered_aeroplanes = filter_aeroplanes(airplane_list, ["United States"])
    assert filtered_aeroplanes[0].country == "United States"
    ranged_aeroplanes = get_aeroplanes_by_altitude(airplane_list, "500 - 7000")
    assert ranged_aeroplanes[0].country == "United States"
    with pytest.raises(ValueError):
        get_aeroplanes_by_altitude(airplane_list, "500 -7000")
    aircraft_sorted_height = sorted_aircraft_height(airplane_list)
    assert aircraft_sorted_height[0].geo_altitude == 13769.34
    top_aeroplanes_height = aircraft_sorted_height[0:1]
    assert top_aeroplanes_height[0].country == "United States"
