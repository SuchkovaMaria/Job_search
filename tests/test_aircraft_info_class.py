from unittest.mock import patch

import pytest

from src.aircraft_info_class import AirplaneInfo
from src.class_request_api import Aircraft


@patch("requests.get")
def test_aircraft_info(mock_requests, coord, list_aircraft_1, dict_1):
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.side_effect = [coord, dict_1, list_aircraft_1]

    aircraft = Aircraft()
    aircraft.get_coordinates("canada")
    airplane_list = AirplaneInfo.list_aircraft(aircraft)
    assert len(airplane_list) == 2
    assert airplane_list[0] >= airplane_list[1]
    assert airplane_list[1] <= airplane_list[0]

    with pytest.raises(ValueError):
        assert AirplaneInfo(1, 1, "hjfg", "gfh")
    with pytest.raises(ValueError):
        assert AirplaneInfo("jf", 1, 1, "gfh")

    assert AirplaneInfo("jf", "canada", 1, "gfh").geo_altitude == 0
