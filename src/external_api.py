import os
from http.client import responses
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """ Принимает транзакцию и возвращает ее сутту в рублях.
    Если валюта USD или EUR -> конвертирует сумму через ERD API"""
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0.0))
    currency = operation_amount.get("currency", {}).get("code", "RUB")

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        api_key = os.getenv("API_KEY")
        url = "https://apilayer.com"
        params = {
            "to": "RUB",
            "from": currency,
            "amount": amount
        }
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()
        return float(result["result"])

    return amount
