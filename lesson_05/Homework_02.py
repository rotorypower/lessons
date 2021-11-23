"""Реализуйте алгоритм игры “Тайный Санта (Secret Santa)”- в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна используя список имен участников выдать на выходе пары, кто и кому будет дарить,
причем сам себе человек не может подарить, дубликаты тоже не допустимы."""


from random import shuffle

secret_santa = ["Дима", "Света ", "Юра", "Катя", "Веня", "Стас"]

def partners(secret_santa):
    number_of_people = len(secret_santa)
    number_of_groups = number_of_people / 2
    if number_of_people % 2 == 1:
        raise ValueError(" Участников должно быть четное количество.")
    for group in range(int(number_of_groups)):
        group_number = group + 1
        first_index = group * 2
        second_index = group * 2 + 1
        print(f"Пара {group_number}: {secret_santa[first_index]} для {secret_santa[second_index]}")


shuffle(secret_santa)
partners(secret_santa)

