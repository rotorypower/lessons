"""Известно, что на шахматной доске 8×8 можно расставить ферзей так,
чтобы они не били друг друга (ферзь может ходить по горизонтали, вертикали и диагонали).
Вам дана расстановка двух ферзей на доске, определите могут ли ферзи бить друг друга.
Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали. Если ферзи не бьют друг друга, выведите слово NO,
иначе выведите YES."""

import math

def chek_caders(x1: int ,y1: int ,x2: int,y2:int ) -> bool:
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


if __name__ == "__main__":
    x1 = int(input("enter x1: "))
    y1 = int(input("enter y1: "))

    x2 = int(input("enter x2: "))
    y2 = int(input("enter y2: "))

    if chek_caders(x1, y1, x2, y2):
        print("Yes")
    else:
        print("No")

