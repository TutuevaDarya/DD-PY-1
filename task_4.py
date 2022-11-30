import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(in_f) -> list[dict]:
    list_line = []
    delimiter = ","
    new_line = "\n"
    list_keys = []
    values = []
    list_values = []
    diction = {}
    list_done = []
    with open(in_f) as f:
        for line in f:
            list_line.append(line.rsplit())
    for line_ in list_line:
        if line_ == list_line[0]:
            list_keys = line_[0].split(delimiter)
        else:
            values.append(line_)
    for value in values:
        list_values.append(value[0].split(delimiter))
    for i in range(len(list_line)-1):
        list_line_i = list_values[i]
        for key in range(len(list_keys)):
            diction[list_keys[key]] = list_line_i[key]
        list_done.append(diction.copy())
    return list_done


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
