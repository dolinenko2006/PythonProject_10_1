from src.widget import mask_account_card, get_date
import pytest


def test_mask_account_card():
    assert mask_account_card("Visa 1111111111111111") == "Visa 1111 11** **** 1111"

def test_get_date():
    assert get_date("1111-11-11T00:00:00.00000") == "11.11.1111"
