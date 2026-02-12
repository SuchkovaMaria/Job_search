from abc import ABC, abstractmethod

import pycountry
import requests


class RequestAPI(ABC):
    """Абстрактный класс определяющий общие методы с запросом API"""

    @abstractmethod
    def get_coordinates(self, country: str) -> None:
        """Метод получения координат"""
        pass

    @abstractmethod
    def _get_aeroplanes(self, geo_coordinates: list) -> None:
        """Метод получения списка самолетов по координатам"""
        pass


class Aircraft(RequestAPI):
    """Класс Самолеты (получение данных из API)"""

    def __init__(self) -> None:
        """Конструктор запросов страны и информации по самолетам"""

        self.__openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.__opensky_url = "https://opensky-network.org/api/states/all?"
        self.__aeroplanes = None

    @property
    def aeroplanes(self) -> list | None:
        """Вывод списка самолетов"""

        return self.__aeroplanes

    def get_coordinates(self, country: str) -> None:
        """Метод получения координат"""

        test = pycountry.countries.get(name=country)
        if test is None:
            raise ValueError("Неправильно введено название страны")
        else:
            country = test.name

            headers_nominatim = {
                "User-Agent": "test-app/1.0",
            }

            params_nominatim = {
                "country": country,
                "format": "json",
                "limit": 1,
            }

            response = requests.get(url=self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
            if response.status_code != 200:
                raise ConnectionError("Ошибка получения координат страны")
            else:
                data = response.json()
                geo_coordinates = data[0].get("boundingbox")
                self._get_aeroplanes(geo_coordinates)

    def _get_aeroplanes(self, geo_coordinates: list) -> None:
        """Метод получения списка самолетов по координатам"""

        params = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        response = requests.get(url=self.__opensky_url, params=params)
        if response.status_code != 200:
            raise ConnectionError("Ошибка получения списка самолетов")
        else:
            self.__aeroplanes = response.json()["states"]
