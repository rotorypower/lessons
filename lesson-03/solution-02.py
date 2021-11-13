#Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Рассчитать сумму на счету пользователя по окончании вклада и вывести на печать, если в конце каждого года ему начисляется бонус в размере 120 рублей.

#option1
money = 2130 
period = 5 
tax = 0.1
bonus = 120 

while period > 0: 
    money += money * tax + bonus 
    period -=1

print (money)

#opion02
#money01 = money + ( money * tax ) + bonus
#money02 = money01 + ( money01 * tax ) + bonus
#money03 = money02 + ( money02 * tax ) + bonus
#money04 = money03 + ( money03 * tax ) + bonus
#money05 = money04 + ( money04 * tax ) + bonus

#print (money05)

