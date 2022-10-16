salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
for delta in range (1, months+1):
    delta = spend - salary #разница между затратами и зп, необходимая в накоплениях, чтобы прожить этот месяц
    spend *= 1 + increase #индексируем затраты на следующий месяц
    need_money += delta #формируем наши накопления
print(round(need_money))
