import json
import logging
import os
from typing import Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "utils.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path: str) -> list[dict[str, Any]]:
    """ Читает json файл с транзакциями и возврашает список словарей,
    а если файл не найден или содержит не список -> возвращает пустой список"""
    if not os.path.exists(file_path):
        logger.warning(f"Файл не найден по пути: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf_8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружены транзакции из файла: {file_path}")
                return data
            logger.warning(f"Данные в файле {file_path} не являются списком")
            return []
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []
