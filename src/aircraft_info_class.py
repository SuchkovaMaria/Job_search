from typing import Any, Self

import pycountry

from src.class_request_api import Aircraft


class AirplaneInfo:
    """Класс информации по самолету"""

    __slots__ = ["identifier", "country", "velocity_speed", "geo_altitude"]

    def __init__(self, identifier: str, country: str, velocity_speed: float | int, geo_altitude: float | int) -> None:
        """Конструктор информации по самолету"""

        self.identifier = self.__control_str(identifier)
        self.country = self.__control_country(country)
        self.velocity_speed = self.__control_float(velocity_speed)
        self.geo_altitude = self.__control_float(geo_altitude)

    def __ge__(self, other: Self) -> bool:
        """Метод сравнения скорости самолетов"""

        return self.velocity_speed >= other.velocity_speed

    def __le__(self, other: Self) -> bool:
        """Метод сравнения высоты самолетов"""

        return self.geo_altitude <= other.geo_altitude

    @staticmethod
    def __control_str(string: str | Any) -> str:
        """Верификация атрибутов с типом str"""
        if not isinstance(string, str):
            raise ValueError("Не передано")
        else:
            string = string.lower()
        return string

    @staticmethod
    def __control_country(string: str | Any) -> str:
        """Верификация атрибутa country"""

        if not isinstance(string, str):
            raise ValueError("Не передано")
        else:
            test = pycountry.countries.get(name=string)
            if test is None:
                raise ValueError("Неправильно введено название страны здесь")
            elif string.lower() == test.name.lower():
                string = test.name
        return string

    @staticmethod
    def __control_float(numbers: float | int | Any) -> float | int:
        """Верификация атрибутов с типом float или int"""
        if not isinstance(numbers, float | int):
            numbers = 0
        else:
            numbers = numbers
        return numbers

    @staticmethod
    def list_aircraft(aircraft: Aircraft) -> list:
        """Получение списка информации по самолетам полученных из API(класс Aircraft)"""

        list_aircraft = []
        for airplane in aircraft.aeroplanes:
            try:
                plane = AirplaneInfo(airplane[0], airplane[2], airplane[9], airplane[13])
                list_aircraft.append(plane)
            except ValueError:
                pass

        return list_aircraft
