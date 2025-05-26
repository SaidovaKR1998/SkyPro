import pytest
from src.widget import mask_account_card, get_date


# Фикстуры для тестовых данных mask_account_card
@pytest.fixture
def valid_cards():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
        ("MasterCard 5555555555554444", "MasterCard 5555 55** **** 4444")
    ]


@pytest.fixture
def card_length_variations():
    return [
        ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),  # 16
        ("Карта 12345678901234567", "Карта 1234 56** **** 4567"),  # 17
        ("Карта 123456789012345678", "Карта 1234 56** **** 5678"),  # 18
        ("Карта 1234567890123456789", "Карта 1234 56** **** 6789")  # 19
    ]


@pytest.fixture
def valid_accounts():
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Account 12345678901234567890", "Account **7890")
    ]


@pytest.fixture
def invalid_inputs():
    return [
        ("", ""),
        ("Просто текст без номера", "Просто текст без номера"),
        ("Счет 123", "Счет 123"),
        ("Карта 1234abcd5678efgh", "Карта 1234abcd5678efgh"),
        ("Карта 1234 5678 9012 abcd", "Карта 1234 5678 9012 abcd")
    ]


# Фикстуры для тестовых данных get_date
@pytest.fixture
def valid_dates():
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("2020-02-29T00:00:00.000000", "29.02.2020")
    ]


@pytest.fixture
def invalid_dates():
    return [
        ("2024-13-11T02:26:18", ""),
        ("2024-03-32T02:26:18", ""),
        ("2023-02-29T00:00:00", ""),
        ("2024-04-31T00:00:00", "")
    ]


@pytest.fixture
def malformed_dates():
    return [
        ("", ""),
        ("2024-03-11", ""),
        ("11.03.2024T02:26:18", ""),
        ("abcdefgh", "")
    ]


# Параметризованные тесты для mask_account_card
@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Invalid 123", "Invalid 123"),
    ("", "")
])
def test_mask_account_card_parametrized(input_str, expected):
    assert mask_account_card(input_str) == expected


# Основные тесты для mask_account_card
def test_mask_account_card(valid_cards, card_length_variations, valid_accounts, invalid_inputs):
    # Тестирование валидных карт
    for card, expected in valid_cards:
        assert mask_account_card(card) == expected

    # Тестирование разной длины номеров карт
    for card, expected in card_length_variations:
        assert mask_account_card(card) == expected

    # Тестирование счетов
    for account, expected in valid_accounts:
        assert mask_account_card(account) == expected

    # Тестирование некорректных данных
    for input_str, expected in invalid_inputs:
        assert mask_account_card(input_str) == expected


# Тестирование обработки исключений для mask_account_card
def test_mask_account_card_exceptions():
    """Теперь проверяем, что функция НЕ вызывает исключения для некорректных данных"""
    # Для карт с буквами - возвращает исходную строку
    assert mask_account_card("Карта 1234abcd5678efgh") == "Карта 1234abcd5678efgh"

    # Для коротких номеров - возвращает исходную строку
    assert mask_account_card("Карта 123456789012345") == "Карта 123456789012345"


# Параметризованные тесты для get_date
@pytest.mark.parametrize("date_str, expected", [
    ("2024-01-01T00:00:00", "01.01.2024"),
    ("2023-12-31T23:59:59", "31.12.2023"),
    ("", ""),
    ("invalid", "")
])
def test_get_date_parametrized(date_str, expected):
    assert get_date(date_str) == expected


# Основные тесты для get_date
def test_get_date(valid_dates, invalid_dates, malformed_dates):
    # Тестирование валидных дат
    for date_str, expected in valid_dates:
        assert get_date(date_str) == expected

    # Тестирование некорректных дат
    for date_str, expected in invalid_dates:
        assert get_date(date_str) == expected

    # Тестирование неправильных форматов
    for date_str, expected in malformed_dates:
        assert get_date(date_str) == expected


# Тестирование обработки исключений для get_date
def test_get_date_exceptions():
    """Проверяем, что функция НЕ вызывает исключения для некорректных дат"""
    # Для несуществующих дат - возвращает пустую строку
    assert get_date("2024-13-11T00:00:00") == ""
    assert get_date("2023-02-29T00:00:00") == ""
