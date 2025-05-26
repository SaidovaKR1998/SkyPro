import json
from typing import List, Dict


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает список транзакций из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу с транзакциями

    Returns:
        Список словарей с транзакциями. Если файл не найден, пустой или содержит не список,
        возвращает пустой список.
    """
    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            # Загружаем данные из JSON
            data = json.load(file)

            # Проверяем, что данные - это список
            if isinstance(data, list):
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        # Если файл не найден или невалидный JSON
        return []

transactions = load_transactions('../data/operations.json')
print(f"Загружено {len(transactions)} транзакций")

