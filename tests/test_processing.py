from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state():
    assert filter_by_state([]) == None


def test_sort_by_date():
    assert sort_by_date([]) == None