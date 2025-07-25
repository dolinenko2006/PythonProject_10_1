def filter_by_state(list_of_dict: list, value_: str = "EXECUTED") -> list:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED')"""
    new_list_of_dict = []  # список словарей, где все ключи 'state' имеют значение value_
    for i in list_of_dict:
        if i["state"] == value_:
            new_list_of_dict.append(i)

    return new_list_of_dict


def sort_by_date(list_of_dict: list, descending: bool = True) -> list:
    """принимает список словарей и необязательный параметр.
    Функция должна возвращать новый список, отсортированный по дате (date).
    (сортировка по убыванию, т.е. сначала самые последние операции)"""
    for dict_ in list_of_dict:
        date_str = dict_["date"][:10].replace("-", "")  # '2018-06-30T02:08:58.425572' -> '20180630'
        date_int = int(date_str)  # строка '20180630' -> число 20180630
        dict_["date_int"] = date_int  # помещаем в словарь ключ ('date_int') = значение (число 20180630)

    sorted_list = sorted(list_of_dict, key=lambda i: i["date_int"], reverse=descending)

    for dict_ in sorted_list:
        del dict_["date_int"]

    return sorted_list
