from typing import Any

import pytest  # type: ignore

from src.processing import filter_by_state, sort_by_date

list_of_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
list_of_dict_same_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},  # повторяющиеся даты
    {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},  # повторяющиеся даты
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state_manual_1(empty_word: str) -> None:
    assert filter_by_state([]) == empty_word


def test_filter_by_state_manual() -> None:
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert (
        filter_by_state(
            [
                {"id": 1, "state": "EMPTY-1", "date": "2018-10-14"},
                {"id": 2, "state": "EMPTY-2", "date": "2018-10-14"},
                {"id": 3, "state": "EMPTY-3", "date": "2018-10-14"},
            ]
        )
        == "Проверьте правильность ввода данных"
    )


@pytest.mark.parametrize(
    "list_of_dict, state, result",
    [
        (
            list_of_dict,
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            list_of_dict,
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (list_of_dict, "EXEMPLE", "Проверьте правильность ввода данных"),
        (list_of_dict, None, "Проверьте правильность ввода данных"),
    ],
)
def test_filter_by_state(list_of_dict: list[dict[str, Any]], state: str, result: list[dict[str, Any]] | str) -> None:
    assert filter_by_state(list_of_dict, state) == result


def test_sort_by_date(list_of_dict_true: list[dict[str, Any]]) -> None:
    assert sort_by_date([]) == "Проверьте правильность ввода данных"
    assert (sort_by_date(list_of_dict, True)) == list_of_dict_true


def test_sort_by_date_1(list_of_dict_false: list[dict[str, Any]]) -> None:
    assert (sort_by_date(list_of_dict, False)) == list_of_dict_false


def test_sort_by_date_with_same_date(list_of_dick_with_same_dates: list[dict[str, Any]]) -> None:
    assert (sort_by_date(list_of_dict_same_date)) == list_of_dick_with_same_dates
