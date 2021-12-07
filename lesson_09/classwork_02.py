"""Создать новый класс Cat, который имеет все те же атрибуты что и Dog,
только заменить метод bark на meow.

Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. У
наследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы,
которые имеются у родительского класса. Создать объект каждого класса и вызвать все его методы.
"""

class Animal:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def change_name(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def guard(self):
        print(f"GUARG {self.name}")

class Cat(Animal):
    def __init__(self,height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def meow(self):
        print(f"MEOW {self.name}")


if __name__ == "__main__":

    dog = Dog(100, 90 , "Shakik", 3)
    cat = Cat(5, 2, "Juja", 2)

    print(dog.name)
    print(dog.height)
    print(dog.age)
    print(dog.weight)
    dog.guard()

    print(cat.name)
    print(cat.height)
    print(cat.weight)
    print(cat.age)
    cat.meow()
