from unittest.mock import patch

import pytest

from src.class_request_api import Aircraft


@patch("requests.get")
def test_classes(mock_requests, coord, list_aircraft_1, dict_1):
    mock_requests.return_value.status_code = 200
    mock_requests.return_value.json.side_effect = [coord, dict_1, list_aircraft_1]

    aircraft = Aircraft()
    aircraft.get_coordinates("canada")
    assert aircraft.aeroplanes[0] == [
        "a7b08d",
        "LXJ595  ",
        "United States",
        1770837787,
        1770837787,
        -100.8456,
        42.6855,
        13716,
        False,
        267.21,
        127.33,
        -0.33,
        None,
        13769.34,
        None,
        False,
        0,
    ]


@patch("requests.get")
def test_classes_2(mock_requests):
    mock_requests.return_value.status_code = 400
    aircraft = Aircraft()
    with pytest.raises(ConnectionError):
        aircraft.get_coordinates("canada")
    with pytest.raises(ConnectionError):
        aircraft._get_aeroplanes([1, 2, 2, 3])
    with pytest.raises(ValueError):
        aircraft.get_coordinates("gfkj")
