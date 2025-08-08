import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(empty_word):
    assert get_mask_card_number(1111111111111111) == '1111 11** **** 1111'
    assert get_mask_card_number(555555) == empty_word
    assert get_mask_card_number(1234567891011121314) == empty_word
    assert get_mask_card_number('123ab') == empty_word
    assert get_mask_card_number() == empty_word


def test_get_mask_account(empty_word):
    assert get_mask_account(22222222222222222222) == '**2222'
    assert get_mask_account(222222) == empty_word
    assert get_mask_account(3333333333333333333) == empty_word
    assert get_mask_account('123ab') == empty_word
    assert get_mask_account() == empty_word
