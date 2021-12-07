"""Создать класс Car.
 Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
 Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
 отображение скорости, задния ход (изменение знака скорости).
"""
max_km = int(input ("Ваша максимальная скорость : "))
min_km = int(input ("На сколько снизить скорость: "))

class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed


    def speed_increase(self):
        self.speed = max_km
        print(f'Speed max : {self.speed}')


    def speed_decrease(self):
        self.speed = max_km - min_km
        print(f'Speed decrease : {self.speed}')


    def stop(self):
        self.speed = max_km - max_km
        print(f"Stop: {self.speed}")

    def speed_display(self):
        print(f"Display speed: {self.speed}")

    def revers(self):
        self.speed =-max_km
        print(f'Revers Speed: {self.speed}')


if __name__ == "__main__":

    cars = Car("BMW", 540, 2001, 0)

    cars.speed_increase()
    cars.speed_decrease()
    cars.stop()
    cars.revers()
    cars.speed_display()

    print((cars.make), (cars.model), (cars.year), (cars.speed))






