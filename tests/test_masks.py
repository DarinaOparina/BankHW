import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected",
                         [
                             ("6767 9999 6767 9999", "6767 99** **** 9999"),
                             ("6767999967679999", "6767 99** **** 9999")

                         ]
)
def test_get_mask_card_number_success(card_number, expected):
    """Тест правильно введенного номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_card",
                         [
                             "7777 9999 6767 999",
                             "9999 6767 7777 99999",
                             ""
                         ]
)
def test_get_mask_card_number_invalid(invalid_card):
    """Тест неправильно введенного номера карты"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(invalid_card)


@pytest.mark.parametrize("account_number, expected",
                         [
                             ("77779999676799997777", "**7777"),
                             ("7777", "**7777")
                         ]
)
def test_get_mask_account_number_success(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("invalid_account",
                         [
                             "999",
                             "",
                             "777s"
                         ]
)
def test_get_account_number_invalid(invalid_account):
    with pytest.raises(ValueError, match="Номер счёта должен содержать только цифры (минимум 4)"):
        get_mask_account(invalid_account)
