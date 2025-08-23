import ast
import itertools

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

with open("transactions.txt", "r", encoding="utf-8") as f:  # читаем список словарей из текстового документа
    data = f.read()
transactions = ast.literal_eval(data)


def test_filter_by_currency(dict_USD):
    assert list(filter_by_currency(transactions)) == dict_USD
    assert list(filter_by_currency(transactions, "USD")) == dict_USD


def test_filter_by_currency_1(dict_RUB):
    assert list(filter_by_currency(transactions, "RUB")) == dict_RUB


def test_filter_by_currency_2():
    with pytest.raises(ValueError) as excinfo:
        list(filter_by_currency(transactions, "US"))  # неверная валюта
    assert "Выберите валюту: USD, RUB" in str(excinfo.value)


def test_transaction_descriptions():
    generation = transaction_descriptions(transactions)
    assert (next(generation)) == "Перевод организации"
    assert (next(generation)) == "Перевод со счета на счет"
    assert (next(generation)) == "Перевод со счета на счет"
    assert (next(generation)) == "Перевод с карты на карту"
    assert (next(generation)) == "Перевод организации"


def test_card_number_generator():
    assert set(itertools.islice(card_number_generator(1, 5), 5)) == {
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0002",
            "0000 0000 0000 0005",
            "0000 0000 0000 0001",
    }
    assert set(itertools.islice(card_number_generator(6, 10), 5)) == {
            "0000 0000 0000 0010",
            "0000 0000 0000 0006",
            "0000 0000 0000 0007",
            "0000 0000 0000 0008",
            "0000 0000 0000 0009",
    }
