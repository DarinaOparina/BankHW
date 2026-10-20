def filter_by_currency(transactions, currency):
    """Фильтрует транзакцию по заданной валюте"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount") or {}
        currency_info = operation_amount.get("currency") or {}
        if currency_info.get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, stop):
    """Генерирует номера банковских карт в заданном диапазоне"""
    for number in range(start, stop +1):
        card_str = str(number)

        while len(card_str) < 16:
            card_str = "0" + card_str

        block1 = card_str[0:4]
        block2 = card_str[4:8]
        block3 = card_str[8:12]
        block4 = card_str[12:16]

        yield  block1 + " " + block2 + " " + block3 + " " + block4
