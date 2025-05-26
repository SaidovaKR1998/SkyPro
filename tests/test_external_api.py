import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub

@pytest.fixture
def rub_transaction():
    return {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "code": "RUB"
            }
        }
    }

@pytest.fixture
def usd_transaction():
    return {
        "operationAmount": {
            "amount": "10.0",
            "currency": {
                "code": "USD"
            }
        }
    }

def test_convert_rub(rub_transaction):
    assert convert_to_rub(rub_transaction) == 100.0

@patch('src.external_api.get_exchange_rate')
def test_convert_usd(mock_rate, usd_transaction):
    mock_rate.return_value = 75.5  # Мок курса доллара
    assert convert_to_rub(usd_transaction) == 755.0
    mock_rate.assert_called_once_with('USD')
