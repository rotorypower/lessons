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
    def __init__(self, x: int = 0 ,y: int = 0):
        self.x = x
        self.y = y



class Figure:
    def __init__(self, circle, triangle, square):
        self.circle = circle
        self.triangle = triangle
        self.square = square



        #Circle (атрибуты: координаты центра, длина радиуса; методы:нахождение периметра и площади окружности),
class Circle:
    def __init__(self, center_circle, radius_length):
        self.center_circle = center_circle
        self.radius_length = radius_length

    def area(self):
        return 3.14 * self.radius_length

    def perimetr(self):
        return 2 * 3.14 * self.radius_length

#Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.p = (self.point_a + self.point_b + self.point_c) / 2

    def areaTrian(self):
        return math.sqrt(self.p * (self.p - self.point_a) * (self.p - self.point_b) * (self.p - self.point_c))



    def perimetrTrian(self):     # периметр треугольника
        return self.point_a + self.point_b + self.point_c






if __name__ == "__main__":



    my_circle = Circle(0, 4)
    my_triangle = Triangle(2,3,4)


    print(my_circle.area())
    print(my_circle.perimetr())
    print(my_triangle.perimetrTrian())
    print(my_triangle.areaTrian())







