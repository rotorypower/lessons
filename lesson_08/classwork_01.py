"""
Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска).
Создать функцию, которая возвращает новый список со всеми машинами, год выпуска которых больше Х.
"""

from library import CAR_LIST, filter_cars

if __name__ == "__main__":
    year = int(input("Year:"))
    print(filter_cars(CAR_LIST, year))

    print(list(y for y in CAR_LIST if y["year"] < year))
    print(list(filter(lambda x: x["year"] < year, CAR_LIST)))