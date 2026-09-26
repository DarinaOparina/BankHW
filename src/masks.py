def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты.

    Формат маски: XXXX XX** **** XXXX
    """

    cleaned = card_number.replace(" ", "")

    if len(cleaned) != 16 or not cleaned.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    first_four = cleaned[:4]
    next_two = cleaned[4:6]
    last_four = cleaned[12:]

    return f"{first_four} {next_two}** **** {last_four}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета.

    Формат маски: **XXXX (отображаются только последние 4 цифры)
    """

    cleaned = account_number.replace(" ", "")

    if len(cleaned) < 4 or not cleaned.isdigit():
        raise ValueError("Номер счета должен содержать только цифры (минимум 4)")

    last_four = cleaned[-4:]
    return f"**{last_four}"
