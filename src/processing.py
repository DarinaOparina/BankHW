def filter_by_state(data: list[dict[str, str | int]], state: str= "EXECUTED") -> list[dict[str, str | int]]:
    """Фильтрует список словарей по значению ключа 'state'."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict[str, str | int]], is_reverse = True) -> list[dict[str, str | int]]:
    """Сортирует список словарей по ключу 'date'."""
    return sorted(data, key=lambda item: item.get("date", ""), reverse=is_reverse)
