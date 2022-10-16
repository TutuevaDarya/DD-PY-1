list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_meaning=0 #Для будущего сохранения максимального значения списка
pos_meaning=0 #Для сохранения индекса максимального значения списка
for pos, value in enumerate(list_numbers):
    if value > max_meaning:
        max_meaning = value #Ищем максимальное значение
        pos_meaning = pos #Сохраняем позицию максимального значения
index=pos_meaning
a=list_numbers[-1] #Сохраняем значение последнего элемента списка
list_numbers[index] = a #Перемещаем значение а на место с индексом максимального значения
list_numbers[-1]=max_meaning #Перемещаем максимальное значение в конец списка

print(list_numbers)
