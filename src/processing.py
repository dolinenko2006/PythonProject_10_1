from typing import Any


def filter_by_state(list_of_dict: list[dict[str, Any]], value_: str = "EXECUTED") -> list[dict[str, Any]]:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED')"""
    new_list_of_dict = []  # список словарей, где все ключи 'state' имеют значение value_
    for i in list_of_dict:
        if i["state"] == value_:
            new_list_of_dict.append(i)

    return new_list_of_dict


def sort_by_date(list_of_dict: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """принимает список словарей и необязательный параметр.
    Функция должна возвращать новый список, отсортированный по дате (date).
    (сортировка по убыванию, т.е. сначала самые последние операции)"""
    sorted_list = sorted(list_of_dict, key=lambda i: i["date"], reverse=descending)

    return sorted_list
