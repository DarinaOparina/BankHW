from src.masks import get_mask_account, get_mask_card_number

def mask_account_card (data: str) -> str:
    """Маскирует номер карты или счёта"""
    parts = data.split()

    number = parts[-1]

    name = " ".join(parts[:-1])

    if name.lower() == "счёт":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_data (date_str: str) -> str:
    """Преобразует строку с датой в формат ДД.ММ.ГГГГ."""
    date_part = date_str.split("T")[0]

    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"