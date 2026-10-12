import pytest
from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("input_str , expected",
                         [
                             ("Visa Platinum 7777999967679999", "Visa Platinum 7777 99** **** 9999"),
                             ("Maestro 7777999967679999", "Maestro 7777 99** **** 9999"),
                             ("Black 77779999676799997777", "Black **7777")
                         ]
)
def test_mask_account_card_success(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("invalid_input",
                         [
                             "Счет 67",
                             "Visa 9999",
                             "Unknown "
                         ]
)
def test_mask_account_card_errors(invalid_input):
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)


@pytest.mark.parametrize("date_str, expected",
                         [
                             ("2005-07-22T02:26:18.671407", "22.07.2005"),
                             ("2022-02-24T05:00:00", "24.02.2022"),
                         ]
)
def test_get_data_success(date_str, expected):
    assert get_data(date_str) == expected


@pytest.mark.parametrize("invalid_date",
                         [
                             "",
                             "2005/07/22"
                         ]
)
def test_get_data_invalid(invalid_date):
    with pytest.raises(ValueError):
        get_data(invalid_date)