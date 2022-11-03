from random import randint  # Импортируем генератор целых случайных чисел


def get_unique_list_numbers(lower=-10, higher=10, length=15):  # Обозначаем диапазон значений и длину списка генерации
    finished = []  # Создаем пустой список, куда будут добавляться случайные неповторяющиеся значения
    been_seen = set()  # Создаем список для случайных значений, которые уже выпадали
    for i in range(length):
        number = randint(lower, higher)  # Генерируем случайное целое число в нужном диапазоне
        while number in been_seen:  # Ставим проверку, выпадало ли такое число ранее
            number = randint(lower, higher)  # Если число выпадало, генериурем еще раз
        been_seen.add(number)  # Добавляем выпавшее число во множество выпадавших
        finished.append(number)  # Добавляем уникальное выпавшее число в наш список
    return finished  # Возвращаем список с уникальными целыми случайными числами указанного диапазона в количестве 15


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
