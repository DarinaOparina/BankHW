import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "masks.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты.

    Формат маски: XXXX XX** **** XXXX
    """

    cleaned = card_number.replace(" ", "")

    if len(cleaned) != 16 or not cleaned.isdigit():
        logger.error(f"Некорректный номеркарты: {card_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    first_four = cleaned[:4]
    next_two = cleaned[4:6]
    last_four = cleaned[12:]

    masked = f"{first_four} {next_two}** **** {last_four}"
    logger.info(f"Номер карты успешно замаскирован: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета.

    Формат маски: **XXXX (отображаются только последние 4 цифры)
    """

    cleaned = account_number.replace(" ", "")

    if len(cleaned) < 4 or not cleaned.isdigit():
        logger.error(f"Некорректный номер счета: {account_number}")
        raise ValueError("Номер счета должен содержать только цифры (минимум 4)")

    last_four = cleaned[-4:]
    masked = f"**{last_four}"
    logger.info(f"Номер счета успешно замаскирован: {masked}")
    return masked
