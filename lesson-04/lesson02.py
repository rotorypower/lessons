#Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран. Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево

polin = str(input( "Введите слово: "))

polin_test = polin[::-1]

if polin == polin_test:
    print("YES")
else:
    print("NO")
