from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str= "EXECUTED") -> list[dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    return [item for item in data if item.get("state") == state]
