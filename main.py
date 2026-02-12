from src.aircraft_info_class import AirplaneInfo
from src.class_request_api import Aircraft
from src.utils import filter_aeroplanes, get_aeroplanes_by_altitude, sorted_aircraft_height


def main():
    """Функция взаимодействия с пользователем"""

    try:
        country = input("Введите название страны (на английском языке): ").lower()
        aircraft = Aircraft()
        aircraft.get_coordinates(country)
        airplane_list = AirplaneInfo.list_aircraft(aircraft)
        if len(airplane_list) == 0:
            print("Не найдено самолетов в зоне заданой страны")
        else:
            filter_words = input(
                "Введите названия стран для фильтрации по стране регистрации (на английском языке): "
            ).split()
            if filter_words != []:
                filtered_aeroplanes = filter_aeroplanes(airplane_list, filter_words)

            altitude_range = input("Введите диапазон высот полета (начальное значение - конечное значение): ")
            if altitude_range != "":
                ranged_aeroplanes = get_aeroplanes_by_altitude(airplane_list, altitude_range)
                if len(ranged_aeroplanes) == 0:
                    print(
                        "Не найдено самолетов в выбраном диапазоне высот\n"
                        "Топ самолетов будет выведен по всем найденым самолетам"
                    )
                    aircraft_sorted_height = sorted_aircraft_height(airplane_list)
                else:
                    aircraft_sorted_height = sorted_aircraft_height(ranged_aeroplanes)
            else:
                print("Не указан диапазон высот\nТоп самолетов будет выведен по всем самолетам")
                aircraft_sorted_height = sorted_aircraft_height(airplane_list)

            top_n = int(input("Введите количество самолетов для вывода в топ N: "))
            top_aeroplanes_height = aircraft_sorted_height[0:top_n]

            print(f"Топ-{top_n} самолетов по высоте:")
            count = 1
            for aeroplane in top_aeroplanes_height:
                print(f"{count}. Борт: {aeroplane.identifier}  (высота: {aeroplane.geo_altitude})")
                count += 1

    except ConnectionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
