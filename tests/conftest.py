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
