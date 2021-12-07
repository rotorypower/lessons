"""Создать класс Car.
 Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
 Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
 отображение скорости, задния ход (изменение знака скорости).
"""


class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed


    def speed_increase(self):
        self.speed = (self.speed) + 60
        print(f'Speed max : {self.speed}')

    def speed_decrease(self):
        self.speed = (self.speed) - 10
        print(f'Speed decrease : {self.speed}')

    def stop(self):     # Если скорость равна 0 , то revers показывает тоже ноль
        self.speed = 10
        print(f"Stop: {self.speed}")

    def speed_display(self):
        print(f"Display speed: {self.speed}")

    def revers(self):

        self.speed = -(self.speed)
        print(f'Revers Speed: {self.speed}')


if __name__ == "__main__":
    cars = Car("BMW", 540, 2001, 0)
    cars.speed_increase()
    cars.speed_decrease()
    cars.stop()
    cars.speed_display()
    cars.revers()

    print((cars.make), (cars.model), (cars.year), (cars.speed))


    cars = Car("Mazda", "RX8", 2010, 0)
    cars.speed_increase()
    cars.speed_decrease()
    cars.stop()
    cars.speed_display()
    cars.revers()


