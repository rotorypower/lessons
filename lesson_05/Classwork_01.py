#Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


def my_format(name):
    result_string = f"Hello, {name}"
    return result_string

my_list = ["Olga", "Alex", "Vano", "Vika", "Dima"]
for name in my_list:
    result = my_format(name)
    print(result)

