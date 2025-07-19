from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_card_number(1111111111111111))  # 16-ти значное число
print(get_mask_account(22222222222222222222))  # 20-ти значное число
print(mask_account_card("Visa 1111111111111111"))
print(get_date("2222-22-22"))
