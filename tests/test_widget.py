from src.widget import mask_account_card, get_date
import pytest


def test_mask_account_card():
    assert mask_account_card("Visa 1111111111111111") == "Visa 1111 11** **** 1111"
    assert mask_account_card("Счет 1111111111111111") == "Счет Номер счета состоит из 20 цифр, а Вы ввели 16"
    assert mask_account_card("Счет 11111111111111111111") == "Счет **1111"
    assert mask_account_card("") == " Номер карты состоит из 16 цифр, а Вы ввели 0"

@pytest.mark.parametrize("my_input, expected_result",
                         [
                             ("Visa 1111111111111111", "Visa 1111 11** **** 1111"),
                             ("Счет 1111111111111111", "Счет Номер счета состоит из 20 цифр, а Вы ввели 16"),
                             ("Счет 11111111111111111111", "Счет **1111"),
                             ("", " Номер карты состоит из 16 цифр, а Вы ввели 0")
                         ]
                         )
def test_mask_account_card(my_input, expected_result):
    assert mask_account_card(my_input) == expected_result



def test_get_date():
    assert get_date("1111-11-11T00:00:00.00000") == "11.11.1111"
    assert get_date("1111-11-11") == "11.11.1111"
    assert get_date() == "00.00.0000"
    assert get_date("rewgfdg") == "Проверьте правильность ввода данных"
