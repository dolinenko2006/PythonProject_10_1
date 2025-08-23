import ast

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

print(get_mask_card_number())  # 16-ти значное число
print(get_mask_account("22222222222222222222"))  # 20-ти значное число
print(mask_account_card("Visa 1111111111111111"))
print(mask_account_card("Счёт 11111111111111111111"))  # == "Visa 1111 11** **** 1111"
print(get_date("2024-03-11"))

list_of_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
list_of_dict_2 = [
    {"id": 1, "state": "EMPTY-1", "date": "2018-10-14"},
    {"id": 2, "state": "EMPTY-2", "date": "2018-10-14"},
    {"id": 3, "state": "EMPTY-3", "date": "2018-10-14"},
]
print(filter_by_state(list_of_dict))
print(sort_by_date(list_of_dict))
print("\n" + "=" * 10 + "\n")  # визуальный разделитель

list_of_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(list_of_dict))
print(sort_by_date(list_of_dict))
print("\n" + "=" * 10 + "\n")  # визуальный разделитель


with open("transactions.txt", "r", encoding="utf-8") as f:  # читаем список словарей из текстового документа
    data = f.read()
transactions = ast.literal_eval(data)


list_of_codes = ["USD", "RUB"]
usd_transactions = filter_by_currency(transactions, "RUB")  # запускаем генератор с отфильтрованными словарями
for _ in range(4):
    try:
        print(next(usd_transactions))
    except ValueError:
        print(f"Ошибка выбора валюты: {', '.join(list_of_codes)}")
        break
    except StopIteration:
        print("Список закончился")  # выводим сообщение об окончании итераций
        break
print("\n" + "=" * 10 + "\n")  # визуальный разделитель


descriptions = transaction_descriptions(transactions)  # запускаем генератор с информацией о транзакциях
for i in descriptions:
    print(i)
print("\n" + "=" * 10 + "\n")  # визуальный разделитель


for card_number in card_number_generator(1, 10):  # запускаем генератор рандомных номеров карт
    print(card_number)
