import pytest
from typing import Dict, List
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> List[Dict]:
    """Фикстура: возвращает список тестовых транзакций с разными валютами"""
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
    ]


@pytest.fixture
def sample_transactions_with_descriptions() -> List[Dict]:
    """Фикстура: возвращает транзакции с описаниями для тестирования"""
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]


def test_filter_by_currency_usd(sample_transactions):
    """Тест: фильтрация транзакций по USD должна возвращать только USD-транзакции"""
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 1
    assert next(usd_transactions)["id"] == 3


def test_filter_by_currency_eur(sample_transactions):
    """Тест: фильтрация по EUR должна возвращать только EUR-транзакции"""
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    assert next(eur_transactions)["id"] == 2


def test_filter_by_currency_empty():
    """Тест: при пустом списке транзакций генератор должен завершаться без ошибок"""
    empty_transactions = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(empty_transactions)


def test_filter_by_currency_no_matches(sample_transactions):
    """Тест: если нет подходящих валют, генератор должен завершаться"""
    gbp_transactions = filter_by_currency(sample_transactions, "GBP")
    with pytest.raises(StopIteration):
        next(gbp_transactions)


def test_transaction_descriptions(sample_transactions_with_descriptions):
    """Тест: генератор должен возвращать описания транзакций по порядку"""
    descriptions = transaction_descriptions(sample_transactions_with_descriptions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


def test_transaction_descriptions_empty():
    """Тест: при пустом списке генератор должен завершаться"""
    empty_descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(empty_descriptions)


@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]),
    (9999_9999_9999_9998, 9999_9999_9999_9999, [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]),
])
def test_card_number_generator(start, end, expected):
    """Параметризованный тест: проверка генерации номеров карт в разных диапазонах"""
    generator = card_number_generator(start, end)
    for expected_num in expected:
        assert next(generator) == expected_num


def test_card_number_generator_format():
    """Тест: проверка правильности форматирования номера карты"""
    generator = card_number_generator(123, 123)
    assert next(generator) == "0000 0000 0000 0123"
