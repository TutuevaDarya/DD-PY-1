money_capital = 10000 #накопления
salary = 5000 #зп
spend = 6000 #затраты
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = salary - spend #разница между зп и затратами, которую придется изымать из накоплений
while money_capital + delta >= spend: #проверяем, что на конец месяца не уйдем в минус
    money_capital = money_capital + delta #остаток накоплений по итогам месяца
    spend = spend * (1 + increase) #считаем затраты на след. месяц
    month += 1 #засчитываем, что прожили этот месяц

print(month)
