""" PART 1
Создать класс Dog. Класс имеет четыре атрибута:
height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog,
вызвать все методы объекта и вывести на экран все его атрибуты
PART 2

Добавить в класс Dog метод change_name.
Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""



class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age



    def jump(self):
        print(f"jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def bark(self):
        print(f"Bark {self.name}")

    def change_name(self, name):
        self.name = name


if __name__ == "__main__":
    dog_bob = Dog(100, 100 , "Bob", 10)
    dog_bob.jump()
    dog_bob.change_name("Sharik")


    print(dog_bob.name)
    print(dog_bob.height)
    print(dog_bob.age)
    print(dog_bob.weight)

    dog_sam = Dog(20, 20, "Sam", 5)
    dog_bob.jump()

    print(dog_bob.name)
    print(dog_bob.height)
    print(dog_bob.weight)
    print(dog_bob.age)

