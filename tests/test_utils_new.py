import pytest
import json
import pandas as pd
from pathlib import Path
import tempfile
import os
from unittest.mock import mock_open, patch
from src.utils_new import load_transactions


@pytest.fixture
def test_files():
    # Создаем временные файлы для тестов
    with tempfile.TemporaryDirectory() as temp_dir:
        json_file = os.path.join(temp_dir, "test.json")
        csv_file = os.path.join(temp_dir, "test.csv")
        xlsx_file = os.path.join(temp_dir, "test.xlsx")
        invalid_file = os.path.join(temp_dir, "test.txt")
        nonexistent_file = os.path.join(temp_dir, "nonexistent.json")

        # Создаем тестовые данные
        test_data = [
            {"id": 1, "amount": 100, "description": "Test 1"},
            {"id": 2, "amount": 200, "description": "Test 2"}
        ]

        # Записываем данные в файлы
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)

        df = pd.DataFrame(test_data)
        df.to_csv(csv_file, index=False)
        df.to_excel(xlsx_file, index=False)

        # Создаем невалидный файл
        with open(invalid_file, 'w', encoding='utf-8') as f:
            f.write("invalid content")

        yield {
            "json_file": json_file,
            "csv_file": csv_file,
            "xlsx_file": xlsx_file,
            "invalid_file": invalid_file,
            "nonexistent_file": nonexistent_file,
            "test_data": test_data,
            "temp_dir": temp_dir
        }


def test_load_json(test_files):
    result = load_transactions(test_files["json_file"])
    assert result == test_files["test_data"]


def test_load_csv(test_files):
    result = load_transactions(test_files["csv_file"])
    assert result == test_files["test_data"]


def test_load_xlsx(test_files):
    result = load_transactions(test_files["xlsx_file"])
    assert result == test_files["test_data"]


def test_load_nonexistent_file(test_files):
    result = load_transactions(test_files["nonexistent_file"])
    assert result == []


def test_load_invalid_format(test_files):
    result = load_transactions(test_files["invalid_file"])
    assert result == []


def test_load_json_not_list(test_files):
    # Создаем JSON файл с данными не в виде списка
    single_transaction_file = os.path.join(test_files["temp_dir"], "single.json")
    with open(single_transaction_file, 'w', encoding='utf-8') as f:
        json.dump({"id": 1, "amount": 100}, f)

    result = load_transactions(single_transaction_file)
    assert result == []


def test_load_invalid_json(test_files):
    # Создаем битый JSON файл
    broken_json_file = os.path.join(test_files["temp_dir"], "broken.json")
    with open(broken_json_file, 'w', encoding='utf-8') as f:
        f.write('{"id": 1, "amount": 100')  # незакрытая скобка

    result = load_transactions(broken_json_file)
    assert result == []


def test_load_empty_file(test_files):
    # Создаем пустой файл
    empty_file = os.path.join(test_files["temp_dir"], "empty.json")
    open(empty_file, 'w').close()

    result = load_transactions(empty_file)
    assert result == []


def test_logging_on_success(test_files, caplog):
    load_transactions(test_files["json_file"])
    assert f"Успешно загружено {len(test_files['test_data'])} транзакций из {test_files['json_file']}" in caplog.text


def test_logging_on_error(test_files, caplog):
    load_transactions(test_files["nonexistent_file"])
    assert f"Файл не найден: {test_files['nonexistent_file']}" in caplog.text
