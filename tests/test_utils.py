import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions

def test_load_transactions_success():
    test_data = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
    with patch('builtins.open', mock_open(read_data=test_data)):
        result = load_transactions('dummy_path.json')
        assert len(result) == 2
        assert result[0]['id'] == 1

def test_load_transactions_empty_file():
    with patch('builtins.open', mock_open(read_data='')):
        result = load_transactions('empty.json')
        assert result == []

def test_load_transactions_invalid_json():
    with patch('builtins.open', mock_open(read_data='invalid json')):
        result = load_transactions('invalid.json')
        assert result == []

def test_load_transactions_not_list():
    test_data = '{"id": 1, "amount": 100}'
    with patch('builtins.open', mock_open(read_data=test_data)):
        result = load_transactions('not_list.json')
        assert result == []

