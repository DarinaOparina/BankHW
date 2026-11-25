from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


def test_convert_to_rub_from_rub() -> None:
    """Тест тр-ции в рублях без обращения к API"""
    transaction = {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"}
        }
    }
    assert convert_to_rub(transaction) == 31957.58


@patch("src.external_api.requests.get")
def test_convert_to_rub_from_usd(mock_get: Mock) -> None:
    """" Тест конв-ции из usd -> rub"""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9500.50}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"name": "USD", "code": "USD"}
        }
    }
    assert convert_to_rub(transaction) == 9500.50
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_from_eur(mock_get: Mock) -> None:
    """Тест конв-ции из eur -> rub"""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 10200.75}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"name": "EUR", "code": "EUR"},
        }
    }
    assert convert_to_rub(transaction) == 10200.75
    mock_get.assert_called_once()
