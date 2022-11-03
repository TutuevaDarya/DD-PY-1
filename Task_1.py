from pprint import pprint  # Импортируем pprint

list_numbers = [{"bin": bin(num), "dec": num, "hex": hex(num), "oct": oct(num)}
                for num in range(16)]  # Список словарей с представлениями чисел от 0 до 15 в сист.исчисл.

pprint(list_numbers)
