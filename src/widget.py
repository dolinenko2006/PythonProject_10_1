from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(attribute: [str] = "Счет 00000000000000000000") -> str:
    """
    Возвращать строку с замаскированным номером.
    Visa Platinum 7000792289606361  - входной аргумент
    Visa Platinum 7000 79** **** 6361  - выход функции
    """
    attribute = str(attribute)
    list_attribute = attribute.split(" ")  # ['Счет', '73654108430135874305']
    number = list_attribute[-1]
    words = " ".join(list_attribute[0:-1])

    if list_attribute[0] == "Счет" or list_attribute[0] == "Счёт":
        return f"{words} {get_mask_account(number)}"
    else:
        return f"{words} {get_mask_card_number(number)}"


def get_date(date_: str = "0000-00-00T00:00:00.00000") -> str:
    """
    принимает на вход строку с датой
    "2024-03-11T02:26:18.671407" - входной аргумент
    "11.03.2024" - выход функции
    """

    date_ = str(date_)
    date_ = date_[:10]  # 2024-03-11
    parts = date_.split("-")
    if len(parts) != 3:
        return "Проверьте правильность ввода данных"

    year, month, day = parts  # -> ('2024', '03', '11')

    if isinstance(int(year),int) and  isinstance(int(month), int) and isinstance(int(day), int):
            return f"{day}.{month}.{year}"

    return "Проверьте правильность ввода данных"
