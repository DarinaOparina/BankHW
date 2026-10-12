import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected_ids",
                         [
                             ("EXECUTED", [1, 3]),
                             ("CANCELED", [2]),
                             ("PENDING", [4]),
                         ]
)
def test_filter_by_state(sample_data, state, expected_ids):
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_not_found(sample_data):
    assert filter_by_state(sample_data, "NON_EXISTENT") == []


def test_filter_by_state_empty(empty_data):
    assert filter_by_state(empty_data, "EXECUTED") == []


def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data, is_sort_reverse=True)
    assert result[0]["id"] == 3
    assert result[-1]["id"] == 2


def test_sort_by_date_ascending(sample_data):
    result = sort_by_date(sample_data, is_sort_reverse=False)
    assert result[0]["id"] == 2
    assert result[-1]["id"] == 3


def test_sort_by_date_same_dates():
    same_date_data = [
        {"id": 1, "date": "2023-12-01T10:00:00"},
        {"id": 2, "date": "2023-12-01T10:00:00"},
    ]
    result = sort_by_date(same_date_data)
    assert len(result) == 2


def test_sort_by_date_missing_or_invalid():
    mixed_data = [
        {"id": 1, "date": "2023-12-01T10:00:00"},
        {"id": 2},
    ]
    result = sort_by_date(mixed_data, is_sort_reverse=True)
    assert result[0]["id"] == 1
