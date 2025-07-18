from typing import Union


def mask_account_card(arg: Union[str] = "Visa 0000000000000000") -> str:
    """
    Возвращать строку с замаскированным номером.
    Visa Platinum 7000792289606361  - входной аргумент
    Visa Platinum 7000 79** **** 6361  - выход функции
    """
    a = str(arg)
    str_arg_ = a.split(" ")  # ['Счет', '73654108430135874305']
    number = str_arg_[-1]
    words = str_arg_[0:-1]
    if str_arg_[0] == "Счет" or str_arg_[0] == "Счёт":
        return f"Счет **{number[-4:]}"
    else:
        number_total = number[0:4] + " " + number[5:7] + "**" + " " + "****" + " " + number[-4:]
        words_total = " ".join(words)
        return f"{words_total} {number_total}"


def get_date(arg: Union[str] = "0000-00-00T00:00:00.00000") -> str:
    """
    принимает на вход строку с датой
    "2024-03-11T02:26:18.671407" - входной аргумент
    "11.03.2024" - выход функции
    """
    arg = str(arg)
    date = arg[:10]  # 2024-03-11
    year, month, day = tuple(date.split("-"))  # -> ('2024', '03', '11')
    return f"{day}.{month}.{year}"
