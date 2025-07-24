

def filter_by_state(list_of_dict: list, value_: str = "EXECUTED") -> list:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED')"""
    new_list_of_dict = []  # список словарей все ключи 'state' имеют значение value_
    for i in list_of_dict:
        if i["state"] == value_:
            new_list_of_dict.append(i)

    return new_list_of_dict


def sort_by_date(list_of_dict: list, range: bool = True) -> list:
    """принимает список словарей и необязательный параметр.
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    for i in list_of_dict:
        number = "".join(i["date"][:10].split("-"))  # '2018-06-30T02:08:58.425572' -> '20180630'
        number = int(number)  # строка '20180630' -> число 20180630
        i["date_int"] = number  # помещаем в словарь ключ ('date_int') = значение (число 20180630)

    sorted_list = sorted(list_of_dict, key=lambda i: i["date_int"], reverse=range)

    for i in sorted_list:
        del i["date_int"]

    return sorted_list
