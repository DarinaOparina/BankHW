import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency_usd(sample_transactions):
    """Проверка правильности фильтрации по USD"""
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268


def test_filter_by_currency_rub(sample_transactions):
    """Проверка правильности фильтрации по RUB"""
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["id"] == 41428829


def test_filter_by_currency_empty():
    """Проверка работы с пустым списком"""
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions):
    """Проверка получения правильных описаний"""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет", "Перевод организации"]


def test_transaction_descriptions_empty():
    """Проверка работы с пустым списком"""
    assert list(transaction_descriptions([])) == []


def test_card_number_generator_range_and_format():
    """Проверка правильного заполнения нулями"""
    result = list(card_number_generator(1, 2))
    assert result == ["0000 0000 0000 0001", "0000 0000 0000 0002"]


def test_card_number_generator_single_value():
    """Проверка генерации для одного числа"""
    result = list(card_number_generator(5, 5))
    assert result == ["0000 0000 0000 0005"]
