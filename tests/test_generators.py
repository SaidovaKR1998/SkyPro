import pytest
from typing import Dict, List, Iterator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

### Фикстуры (подготовка тестовых данных) ###
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

### Тесты для filter_by_currency ###
def test_filter_by_currency_usd(sample_transactions):
    """Тест: фильтрация транзакций по USD должна возвращать только USD-транзакции"""
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    # Проверяем, что первая найденная транзакция имеет id=1 (USD)
    assert next(usd_transactions)["id"] == 1
    # Проверяем, что вторая найденная транзакция имеет id=3 (USD)
    assert next(usd_transactions)["id"] == 3

def test_filter_by_currency_eur(sample_transactions):
    """Тест: фильтрация по EUR должна возвращать только EUR-транзакции"""
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    # Должна быть только одна EUR-транзакция с id=2
    assert next(eur_transactions)["id"] == 2

def test_filter_by_currency_empty():
    """Тест: при пустом списке транзакций генератор должен завершаться без ошибок"""
    empty_transactions = filter_by_currency([], "USD")
    # Ожидаем StopIteration, так как транзакций нет
    with pytest.raises(StopIteration):
        next(empty_transactions)

def test_filter_by_currency_no_matches(sample_transactions):
    """Тест: если нет подходящих валют, генератор должен завершаться"""
    gbp_transactions = filter_by_currency(sample_transactions, "GBP")
    # Ожидаем StopIteration, так как GBP-транзакций нет
    with pytest.raises(StopIteration):
        next(gbp_transactions)

### Тесты для transaction_descriptions ###
def test_transaction_descriptions(sample_transactions_with_descriptions):
    """Тест: генератор должен возвращать описания транзакций по порядку"""
    descriptions = transaction_descriptions(sample_transactions_with_descriptions)
    # Проверяем последовательность возвращаемых описаний
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"

def test_transaction_descriptions_empty():
    """Тест: при пустом списке генератор должен завершаться"""
    empty_descriptions = transaction_descriptions([])
    # Ожидаем StopIteration
    with pytest.raises(StopIteration):
        next(empty_descriptions)

### Тесты для card_number_generator ###
@pytest.mark.parametrize("start, end, expected", [
    # Тест 1: проверка генерации одного номера
    (1, 1, ["0000 0000 0000 0001"]),
    # Тест 2: проверка генерации последовательности
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]),
    # Тест 3: проверка генерации крайних значений
    (9999_9999_9999_9998, 9999_9999_9999_9999, [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]),
])
def test_card_number_generator(start, end, expected):
    """Параметризованный тест: проверка генерации номеров карт в разных диапазонах"""
    generator = card_number_generator(start, end)
    # Проверяем каждый ожидаемый номер в последовательности
    for expected_num in expected:
        assert next(generator) == expected_num

def test_card_number_generator_format():
    """Тест: проверка правильности форматирования номера карты"""
    generator = card_number_generator(123, 123)
    # Проверяем, что номер правильно дополняется нулями и форматируется
    assert next(generator) == "0000 0000 0000 0123"