from typing import Optional


def filter_by_state(list_of_dict:list, key:str = 'EXECUTED') -> list:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED')"""
    new_list_of_dict = []
    for i in list_of_dict:
        if i['state'] == key:
            new_list_of_dict.append(i)

    return new_list_of_dict


def sort_by_date(a:list, b:Optional[bool] = True) -> list:
    """принимает список словарей и необязательный параметр.
    Функция должна возвращать новый список, отсортированный по дате (date)."""
    pass

a = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(a,))