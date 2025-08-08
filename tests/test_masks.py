from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number(1111111111111111) == '1111 11** **** 1111'
    assert get_mask_card_number(555555) == 'Номер карты состоит из 16 цифр, а Вы ввели 6'
    assert get_mask_card_number(1234567891011121314) == 'Номер карты состоит из 16 цифр, а Вы ввели 19'
    assert get_mask_card_number('123ab') == 'Номер карты состоит из 16 цифр, а Вы ввели 5'
    assert get_mask_card_number() == 'Номер карты состоит из 16 цифр, а Вы ввели 0'

def test_get_mask_account():
    assert get_mask_account(22222222222222222222) == '**2222'
    assert get_mask_account(222222) == 'Номер счета состоит из 20 цифр, а Вы ввели 6'
    assert get_mask_account(3333333333333333333) == 'Номер счета состоит из 20 цифр, а Вы ввели 19'
    assert get_mask_account('123ab') == 'Номер счета состоит из 20 цифр, а Вы ввели 5'
    assert get_mask_account() == 'Номер счета состоит из 20 цифр, а Вы ввели 0'
