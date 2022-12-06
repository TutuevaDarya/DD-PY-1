import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(in_f, delimiter=',') -> list[dict]:
    with open(in_f, "r") as f:
        headers_list = f.readline()[:-1].split(delimiter)  # выделяем заголовки, читая 1 строку файла и разделяя их
        rows_list = [line[:-1].split(delimiter) for line in f.readlines()]  # создаем список значений строк/рядов, читая строки файла
        return [dict(zip(headers_list, line)) for line in rows_list]  # возвращаем список словарей, где по парам ключ-значение
                              # представлены заголовок и соответствующее значение строки соответствующего списка строк/рядов


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
