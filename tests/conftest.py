import pytest

@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-11-15T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-10T09:30:00"},
        {"id": 4, "state": "PENDING", "date": "2023-12-01T10:00:00"},
    ]

@pytest.fixture
def empty_data():
    return []

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "operationAmount": {"amount": "43573.71", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
        },
    ]
