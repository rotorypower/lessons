#Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
# к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".

def month_to_seasom(month):
    if month == 12 or month == 1 or month == 2:
        return "Winter"
    elif month == 3 or month == 4 or month == 5:
        return "Spring"
    elif month == 6 or month == 7 or month == 8:
        return "Summer"
    elif month == 9 or month == 10 or month == 11:
        return "Autumn"
    elif month == 0 or month > 12:
        return "No such month"

result = month_to_seasom(int(input("Enter month? :")))
print(result)
