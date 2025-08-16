from typing import Union

from src.masks import get_mask_account, get_mask_card_number

list_pay_sistem = ["Maestro", "MasterCard", "Visa", "Visa Classic", "Visa Platinum", "Visa Gold"]


def mask_account_card(attribute: str = "Счет 00000000000000000000") -> str:
    """
    Возвращать строку с замаскированным номером.
    Visa Platinum 7000792289606361  - входной аргумент
    Visa Platinum 7000 79** **** 6361  - выход функции
    """
    attribute = str(attribute)
    list_attribute = attribute.split(" ")  # ['Счет', '73654108430135874305']
    number = list_attribute[-1]
    words = " ".join(list_attribute[0:-1])

    if words in ["Счет", "Счёт"] and len(number) == 20:
        return f"{words} {get_mask_account(number)}"
    elif words in list_pay_sistem and len(number) == 16:
        return f"{words} {get_mask_card_number(number)}"
    else:
        return "Проверьте правильность ввода данных"


def get_date(date_: Union[str, int] = "") -> Union[str, int]:
    """
    принимает на вход строку с датой
    "2024-03-11T02:26:18.671407" - входной аргумент
    "11.03.2024" - выход функции
    """

    date_ = str(date_)
    date_ = date_[:10]  # 2024-03-11
    #    try:
    #        year, month, day = date_.split("-")
    #    except ValueError:
    #        return "Проверьте правильность ввода данных"
    parts = date_.split("-")
    if len(parts) != 3:
        return "Проверьте правильность ввода данных"

    year, month, day = parts  # -> ('2024', '03', '11')

    if year.isdigit() and month.isdigit() and day.isdigit():
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            year_int, month_int, day_int = int(year), int(month), int(day)
            if 0 <= year_int and 1 <= month_int <= 12 and 1 <= day_int <= 31:
                return f"{day_int:02d}.{month_int:02d}.{year_int}"
    return "Проверьте правильность ввода данных"
