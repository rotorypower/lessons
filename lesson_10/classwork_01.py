"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""
from __future__ import annotations


class MyTime:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):    #Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __eq__(self, other: MyTime) -> bool:
        return (
            self.hours == other.hours and
            self.minutes == other.minutes and
            self.seconds == other.seconds
        )

    def __ne__(self, other: MyTime) -> bool:
        return not self.__eq__(other)

    def __ge__(self, other: MyTime) -> bool:
        return (
            self.hours >= other.hours or
            self.minutes >= other.minutes or
            self.seconds >= other.seconds
        )

    def __le__(self, other: MyTime) -> bool:
        return not self.__ge__(other)

    def __gt__(self, other: MyTime) -> bool:
        return (
            self.hours > other.hours or
            self.minutes > other.minutes or
            self.seconds > other.seconds
        )

    def __lt__(self, other: MyTime) -> bool:
        return not self.__gt__(other)


if __name__ == "__main__":
    my_time_1 = MyTime(1, 2, 3)
    my_time_2 = MyTime(1, 2, 3)
    my_time_3 = MyTime(2, 3, 4)

    print(my_time_1 == my_time_2)

    print(my_time_1 == my_time_3)
    print(my_time_1.__eq__(my_time_3))