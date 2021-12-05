"""Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу и что это за элемент.
Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5],
 то на печать программа должна вывести числа 4 и 3, где 4 - повторяющийся элемент, 3 - количество повторений
"""

list_of_numbers = [2,2,3,3,3,7,7,7,44,18,18,18,18,3,3,0]
list_of_numbers = list_of_numbers[:list_of_numbers.index(0)]
max_repeat = 1
result_max = 1
max_repeat_name = list_of_numbers[0]

for i in range(1, len(list_of_numbers)):
    if list_of_numbers[i] == list_of_numbers[i-1]:
        max_repeat += 1
        if result_max < max_repeat:
            result_max = max_repeat
            max_repeat_name = list_of_numbers[i]
    else:
        max_repeat = 1

if name == "main":
    print(f"Число: {max_repeat_name}\nПовторилось: {result_max} раза.")