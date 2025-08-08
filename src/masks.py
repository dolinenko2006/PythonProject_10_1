from typing import Union


def get_mask_card_number(arg: Union[str, int] = '') -> str:
    """принимает на вход номер карты и возвращает ее маску"""

    str_number = str(arg)
    if len(str_number) != 16:
        return "Проверьте правильность ввода данных"
    index_start, index_end = 6, 12
    new_str_number = str_number[:index_start] + "*" * (index_end - index_start) + str_number[index_end:]
    result = f"{new_str_number[:4]} {new_str_number[4:8]} {new_str_number[8:12]} {new_str_number[12:]}"
    return result


def get_mask_account(arg: Union[str, int] = '') -> str:
    """принимает на вход номер счета и возвращает его маску"""

    str_number = str(arg)
    if len(str_number) == 20 and str_number.isdigit():
        return f"**{str_number[-4:]}"

    return "Проверьте правильность ввода данных" # f"Номер счета состоит из 20 цифр, а Вы ввели {len(str_number)}"
