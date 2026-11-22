import json
import os
from typing import Any

def get_transactions(file_path: str) -> list[dict[str, Any]]:
    """ Читает json файл с транзакциями и возврашает список словарей,
    а если файл не найден или содержит не список -> возвращает пустой список"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf_8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []

