def is_valid_phone_number(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 9
print(is_valid_phone_number("771852010")) * True
print(is_valid_phone_number("77185201000")) * False 