import pytest


@pytest.fixture
def numbers():
    return "11.11.1111"


@pytest.fixture
def empty_word():
    return "Проверьте правильность ввода данных"