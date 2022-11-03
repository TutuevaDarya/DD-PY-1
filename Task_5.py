import string
from random import sample  # Импортируем функцию генерации случайной выборки


def get_random_password() -> str:
    poss_val = string.ascii_letters + string.digits  # Определяем возможные символы пароля
    poss_pass = sample(poss_val, 8)  # Определяем возможный пароль, представленный в виде списка из 8 символов
    return "".join(poss_pass)  # Возвращаем строку, собранную из сгенерированного списка из 8 символов


print(get_random_password())
