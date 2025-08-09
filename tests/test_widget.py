import pytest  # type: ignore

from src.widget import get_date, mask_account_card


def test_mask_account_card_manual_1() -> None:
    assert mask_account_card("Visa 1111111111111111") == "Visa 1111 11** **** 1111"
    assert mask_account_card("Счет 11111111111111111111") == "Счет **1111"


def test_mask_account_card_manual(empty_word: str) -> None:
    assert mask_account_card("Счет 1111111111111111") == empty_word
    assert mask_account_card("") == empty_word


@pytest.mark.parametrize(
    "my_input, expected_result",
    [
        ("Visa 1111111111111111", "Visa 1111 11** **** 1111"),
        ("Счет 1111111111111111", "Проверьте правильность ввода данных"),
        ("Счет 11111111111111111111", "Счет **1111"),
        ("", "Проверьте правильность ввода данных"),
    ],
)
def test_mask_account_card(my_input: str, expected_result: str) -> None:
    assert mask_account_card(my_input) == expected_result


def test_get_date_1(numbers: str) -> None:  # используем данные из фикстур
    assert get_date("1111-11-11T00:00:00.00000") == numbers
    assert get_date("1111-11-11") == numbers


def test_get_date(empty_word: str) -> None:  # используем данные из фикстур
    assert get_date() == empty_word
    assert get_date("rewgfdg") == empty_word
