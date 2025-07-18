from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(1111111111111111)) # 16-ти значное число
print(get_mask_account(22222222222222222222)) # 20-ти значное число
