from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number(1111111111111111) == '1111 11** **** 1111'


def test_get_mask_account():
    assert get_mask_account(22222222222222222222) == '**2222'