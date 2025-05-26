import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def valid_card_numbers():
    return [
        "1234567890123456",
        "1234 5678 9012 3456",
        "1111222233334444"
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "123456789012345",   # 15 цифр
        "12345678901234567",  # 17 цифр
        "1234abcd90123456",   # буквы в номере
        "",                   # пустая строка
        "1234 5678 9012 345"  # 15 цифр с пробелами
    ]


@pytest.fixture
def valid_account_numbers():
    return [
        "1234567890",
        "73654108430135874305",
        "1234 5678 9012 3456 7890"
    ]


@pytest.fixture
def invalid_account_numbers():
    return [
        "123",       # меньше 4 цифр
        "12ab34",    # буквы в номере
        "",          # пустая строка
        "1 2 3 4"    # пробелы, но всего 4 цифры
    ]


def test_valid_card_masking(valid_card_numbers):
    """Тестирование корректного маскирования валидных номеров карт"""
    expected = [
        "1234 56** **** 3456",
        "1234 56** **** 3456",
        "1111 22** **** 4444"
    ]

    for number, expected_result in zip(valid_card_numbers, expected):
        assert get_mask_card_number(number) == expected_result


def test_invalid_card_numbers(invalid_card_numbers):
    """Тестирование обработки невалидных номеров карт"""
    for number in invalid_card_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(number)


def test_card_number_edge_cases():
    """Тестирование граничных случаев"""
    # Проверка минимально допустимой длины (16 цифр)
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Проверка обработки None
    with pytest.raises(AttributeError):
        get_mask_card_number(None)

    # Проверка обработки не строковых значений
    with pytest.raises(AttributeError):
        get_mask_card_number(1234567890123456)


def test_valid_account_masking(valid_account_numbers):
    """Тестирование корректного маскирования валидных номеров счетов"""
    expected = [
        "**7890",
        "**4305",
        "**7890"
    ]

    for number, expected_result in zip(valid_account_numbers, expected):
        assert get_mask_account(number) == expected_result


def test_invalid_account_numbers():
    """Тестирование обработки невалидных номеров счетов"""
    test_cases = [
        ("123", ValueError),  # Слишком короткий
        ("12ab34", ValueError),  # Содержит буквы
        ("", ValueError),  # Пустая строка
        ("1 2 3 a", ValueError),  # Пробелы и буквы
        (None, AttributeError),  # None
        (123456, AttributeError)  # Число вместо строки
    ]

    for number, expected_exception in test_cases:
        with pytest.raises(expected_exception):
            get_mask_account(number)


def test_account_number_edge_cases():
    """Тестирование граничных случаев"""
    # Проверка минимально допустимой длины (4 цифры)
    assert get_mask_account("1234") == "**1234"

    # Проверка обработки None
    with pytest.raises(AttributeError):
        get_mask_account(None)

    # Проверка обработки не строковых значений
    with pytest.raises(AttributeError):
        get_mask_account(1234567890)


def test_card_number_formatting():
    """Тестирование правильности форматирования номера карты"""
    masked = get_mask_card_number("1234567890123456")
    parts = masked.split()
    assert len(parts) == 4
    assert parts[0] == "1234"
    assert parts[1] == "56**"
    assert parts[2] == "****"
    assert parts[3] == "3456"


def test_account_number_formatting():
    """Тестирование правильности форматирования номера счета"""
    masked = get_mask_account("1234567890")
    assert masked[:2] == "**"
    assert masked[2:] == "7890"
    assert len(masked) == 6
