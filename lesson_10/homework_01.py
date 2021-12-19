"""Создать класс Point, описывающий точку (атрибуты: x, y).
Создать класс Figure.
Создать три дочерних класса
Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании. """

# задачу не закончил.
import math

class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Figure:
    def __init__(self, circle, triangle, square):
        self.circle = circle
        self.triangle = triangle
        self.square = square


#Circle (атрибуты: координаты центра, длина радиуса; методы:нахождение периметра и площади окружности),
class Circle(Figure):
    def __init__(self, center_circle, radius_length):
        self.center_circle = center_circle
        self.radius_length = radius_length

    def area_circle(self):
        return math.pi * self.radius_length

    def perimetr_circle(self):
        return 2 * math.pi * self.radius_length


#Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
class Triangle(Figure):
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.p = (self.point_a + self.point_b + self.point_c) / 2

    def perimetr_trian(self):  # периметр треугольника
        return self.point_a + self.point_b + self.point_c

    def area_trian(self):
        return math.sqrt(self.p * (self.p - self.point_a) * (self.p - self.point_b) * (self.p - self.point_c))


#Square (атрибуты: две точки, методы: нахождение площади и периметра).
class Square(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area_tquaer(self):
        return self.side_a * self.side_b

    def perimetr_tquaer(self):
        return (self.side_a + self.side_b) * 2




if __name__ == "__main__":

    my_list = [Circle(1, 4), Triangle(2, 2, 2), Square(2, 4)]
    for area_figure in my_list:
        if area_figure == my_list[0]:
            print(f'Площадь круга: {area_figure.area_circle()}')
        elif area_figure == my_list[1]:
            print(f'Площадь треугольника: {area_figure.area_trian()}')
        elif area_figure == my_list[2]:
            print(f'Площадь квадрата: {area_figure.area_tquaer()}')










