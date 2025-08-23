import random

list_of_codes = ["USD", "RUB"]


def filter_by_currency(my_list, code="USD"):
    # принимает на вход список словарей, представляющих транзакции, где валюта операции соответствует заданной
    if code not in list_of_codes:
        raise ValueError(f'Выберите валюту: {", ".join(list_of_codes)}')

    for i in my_list:
        if i["operationAmount"]["currency"]["code"] == code:
            yield i


def transaction_descriptions(my_list):
    # принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    for i in my_list:
        yield i["description"]


def card_number_generator(start=1, stop=5):
    # выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    random_numbers = set()
    while True:
        number = random.randint(start, stop)
        if number in random_numbers:  # проверяем чтобы не было повторений номеров карт
            continue

        random_numbers.add(number)
        str_zero_num = "0" * (16 - len(str(number))) + str(number)
        total_str = str_zero_num[:4] + " " + str_zero_num[4:8] + " " + str_zero_num[8:12] + " " + str_zero_num[12:]
        yield total_str
