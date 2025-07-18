from typing import Union

def mask_account_card(arg: Union[str, int] = 'Visa 0000000000000000') -> str:
    """
    Возвращать строку с замаскированным номером.
    Visa Platinum 7000792289606361  - входной аргумент
    Visa Platinum 7000 79** **** 6361  - выход функции
    """
    a = str(arg)
    str_arg_ = a.split(' ')
    str_number = str_arg_[-1]
    str_number_total = str_number[0:4] + ' ' + str_number[5:7] + '**' + ' ' + '****' + ' ' + str_number[-4:]
    str_words = str_arg_[0:-1]
    str_words_total = " ".join(str_words)
    return f'{str_words_total} {str_number_total}'


def get_date(arg: Union[str, int] = '2024-03-11T02:26:18.671407') -> str:

    """
    принимает на вход строку с датой
    "2024-03-11T02:26:18.671407" - входной аргумент
    "11.03.2024" - выход функции
    """
    arg = str(arg)
    date = arg[:10]
    print(type(date))
    print(date)

    pass

get_date()