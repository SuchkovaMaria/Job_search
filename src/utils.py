def sorted_aircraft_height(aircraft_info: list, sort_order: bool = True) -> list:
    """Функция сортировки списка самолетов по высоте (по умолчанию - по убыванию)"""

    sort_list = sorted(aircraft_info, key=lambda x: x.geo_altitude, reverse=sort_order)
    return sort_list


def filter_aeroplanes(aircraft_info: list, filter_words: list) -> list:
    """Функция фильтрации списка самолетов по списку стран"""

    aircraft_list = []
    for airplane in aircraft_info:
        if airplane.country in filter_words:
            aircraft_list.append(airplane)
    return aircraft_list


def get_aeroplanes_by_altitude(aeroplane_list: list, altitude_hight: str) -> list:
    """Функция фильтрации списка самолетов по диапазону высот"""

    altitude_range = altitude_hight.split(" - ")
    if len(altitude_range) != 2:
        raise ValueError("Неверно введены данные диапазона высоты")
    height_range = [int(num) for num in altitude_range]
    aircraft_list = []
    for airplane in aeroplane_list:
        if height_range[0] < airplane.geo_altitude < height_range[1]:
            aircraft_list.append(airplane)
    return aircraft_list
