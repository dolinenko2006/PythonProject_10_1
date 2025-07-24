# from src.masks import get_mask_account, get_mask_card_number
# from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

# print(get_mask_card_number(1111111111111111))  # 16-ти значное число
# print(get_mask_account(22222222222222222222))  # 20-ти значное число
# print(mask_account_card("Visa 1111111111111111"))
# print(get_date("2222-22-22"))

a = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(a))
print(sort_by_date(a, False))
