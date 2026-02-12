import json
from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Any

from src.aircraft_info_class import AirplaneInfo


class AbstractFileWork(ABC):
    """Абстрактный класс определяющий общие методы по работе с файлом, содержащим
    информацию по самолетам"""

    @abstractmethod
    def add_info_in_file(self, plane_object: AirplaneInfo) -> None:
        """Метод для добавления информации в файл"""
        pass

    @abstractmethod
    def read_info_from_file(self) -> None:
        """Метод для чтения информации из файла"""
        pass

    @abstractmethod
    def delete_info_from_file(self, plane_object: AirplaneInfo) -> None:
        """Метод для удаления информации из файла"""
        pass


class FileWork(AbstractFileWork):
    """Класс работы с файлом, содержащим информацию о самолете"""

    def __init__(self, filename: str = "../data/Airplane.json") -> None:
        """Конструктор создания экземпляра класса FileWork"""
        self.__filename = filename

    @property
    def filename(self) -> str:
        return self.__filename

    def add_info_in_file(self, airplane_info: AirplaneInfo) -> Any:
        """Метод для добавления информации в файл"""

        try:
            with open(self.filename, "a+", encoding="UTF-8") as file:
                file.seek(0)
                try:
                    data = json.load(file)
                except JSONDecodeError:
                    data = []

                plane_dict = {
                    "identifier": airplane_info.identifier,
                    "country": airplane_info.country,
                    "velocity_speed": airplane_info.velocity_speed,
                    "geo_altitude": airplane_info.geo_altitude,
                }

                if plane_dict not in data:
                    data.append(plane_dict)

                file.seek(0)
                file.truncate()
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("В файл добавлена информация о самолете")
        except FileNotFoundError:
            print("Файл не найден")

    def read_info_from_file(self) -> list:
        """Метод для чтения информации из файла"""

        try:
            with open(self.filename, "r", encoding="UTF-8") as file:
                try:
                    data = json.load(file)
                except JSONDecodeError:
                    data = []
                return data

        except FileNotFoundError:
            return []

    def delete_info_from_file(self, airplane_info: AirplaneInfo) -> Any:
        """Метод для удаления информации из файла"""

        try:
            with open(self.filename, "a+", encoding="UTF-8") as file:
                file.seek(0)
                try:
                    data = json.load(file)
                except JSONDecodeError:
                    data = []

                plane_dict = {
                    "identifier": airplane_info.identifier,
                    "country": airplane_info.country,
                    "velocity_speed": airplane_info.velocity_speed,
                    "geo_altitude": airplane_info.geo_altitude,
                }

                new_data = []
                if plane_dict in data:
                    for plane in data:
                        if plane != plane_dict:
                            new_data.append(plane)
                else:
                    new_data = data

                file.seek(0)
                file.truncate()
                json.dump(new_data, file, ensure_ascii=False, indent=4)

            print("Информация о самолете удалена из файла")
        except FileNotFoundError:
            print("Файл не найден")
