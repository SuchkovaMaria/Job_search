import os

from config import PATH_DIR
from src.aircraft_info_class import AirplaneInfo
from src.class_filework import FileWork


def test_filework_1():
    air_1 = "abc", "canada", 1.1, 1.1
    air_2 = "abcd", "canada", 1.2, 1.2
    file = FileWork(PATH_DIR + "/data/Airplane_test.json")
    file_empty = FileWork("")
    file_test = FileWork(PATH_DIR + "/data/test_error.json")
    file.add_info_in_file(AirplaneInfo(*air_1))
    file.add_info_in_file(AirplaneInfo(*air_2))
    assert file.read_info_from_file() == [
        {"country": "Canada", "geo_altitude": 1.1, "identifier": "abc", "velocity_speed": 1.1},
        {"country": "Canada", "geo_altitude": 1.2, "identifier": "abcd", "velocity_speed": 1.2},
    ]
    file.delete_info_from_file(AirplaneInfo(*air_1))
    file.delete_info_from_file(AirplaneInfo(*air_1))
    assert file.read_info_from_file() == [
        {"country": "Canada", "geo_altitude": 1.2, "identifier": "abcd", "velocity_speed": 1.2}
    ]
    os.remove(PATH_DIR + "/data/Airplane_test.json")

    file_empty.add_info_in_file(AirplaneInfo(*air_1))
    file_empty.delete_info_from_file(AirplaneInfo(*air_1))
    assert file_empty.read_info_from_file() == []

    assert file_test.read_info_from_file() == []
