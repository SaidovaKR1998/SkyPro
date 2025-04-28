import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date


# Фикстуры с тестовыми данными
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-10T12:30:45.123456"},
        {"id": 2, "state": "PENDING", "date": "2023-04-09T08:15:27.987654"},
        {"id": 3, "state": "EXECUTED", "date": "2023-04-08T14:22:10.456789"},
        {"id": 4, "state": "CANCELED", "date": "2023-04-07T11:05:33.789012"},
        {"id": 5, "state": "EXECUTED", "date": "2023-04-06T09:45:18.345678"},
        {"id": 6, "date": "2023-04-05T16:33:21.234567"},  # Нет ключа state
        {"id": 7, "state": "EXECUTED", "date": "2023-04-10T12:30:45.123456"},  # Такая же дата как у id 1
    ]


@pytest.fixture
def empty_transactions():
    return []


# Параметризованные тесты для filter_by_state
@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3, 5, 7]),
    ("PENDING", [2]),
    ("CANCELED", [4]),
    ("UNKNOWN", []),
])
def test_filter_by_state(sample_transactions, state, expected_ids):
    filtered = filter_by_state(sample_transactions, state)
    assert [t["id"] for t in filtered] == expected_ids
    assert all(t.get("state") == state for t in filtered)


def test_filter_by_state_default(sample_transactions):
    filtered = filter_by_state(sample_transactions)
    assert [t["id"] for t in filtered] == [1, 3, 5, 7]
    assert all(t.get("state") == "EXECUTED" for t in filtered)


def test_filter_by_state_missing_key(sample_transactions):
    filtered = filter_by_state(sample_transactions, "EXECUTED")
    assert 6 not in [t["id"] for t in filtered]


def test_filter_empty_list(empty_transactions):
    assert filter_by_state(empty_transactions) == []


# Параметризованные тесты для sort_by_date
@pytest.mark.parametrize("reverse, expected_order", [
    (True, [1, 7, 2, 3, 4, 5, 6]),  # По убыванию (новые сначала)
    (False, [6, 5, 4, 3, 2, 1, 7]),  # По возрастанию (старые сначала)
])
def test_sort_by_date(sample_transactions, reverse, expected_order):
    sorted_trans = sort_by_date(sample_transactions, reverse)
    assert [t["id"] for t in sorted_trans] == expected_order


def test_sort_by_date_with_same_dates(sample_transactions):
    sorted_trans = sort_by_date(sample_transactions)
    # Проверяем что записи с одинаковой датой остаются в исходном порядке
    assert sorted_trans[0]["id"] == 1
    assert sorted_trans[1]["id"] == 7


def test_sort_by_date_missing_key():
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])  # Нет ключа 'date'


def test_sort_empty_list(empty_transactions):
    assert sort_by_date(empty_transactions) == []


# Тестирование обработки разных форматов дат
def test_date_formats():
    transactions = [
        {"id": 1, "date": "2023-04-10T12:30:45.123456"},  # ISO с микросекундами
        {"id": 2, "date": "2023-04-10T12:30:45"},  # ISO без микросекунд
        {"id": 3, "date": "2023-04-10"},  # Только дата
    ]

    sorted_trans = sort_by_date(transactions)
    assert [t["id"] for t in sorted_trans] == [1, 2, 3]