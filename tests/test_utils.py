from unittest.mock import mock_open, patch

from src.utils import get_transactions


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_get_transactions_valid(mock_file, mock_exists) -> None:
    """Тест успешного чтения списка транзакций из json"""
    result = get_transactions("data/operations.json")
    assert result == [{"id": 1, "amount": 100}]


@patch("os.path.exists", return_value=False)
def test_get_transactions_file_not_found(mock_exists) -> None:
    """Тест, если файл не найден"""
    assert get_transactions("non_existent.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='{"id": 1}')
def test_get_transactions_not_a_list(mock_file, mock_exists) -> None:
    """Тест, если json содержит не список, а словарь"""
    assert get_transactions("data/operations.json") == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_transactions_empty_file(mock_file, mock_exists) -> None:
    """Тест пустого json-файла"""
    assert get_transactions("data/operations.json") == []
