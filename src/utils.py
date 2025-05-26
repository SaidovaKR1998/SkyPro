import json
from src.log_config import logger

def load_transactions(file_path: str) -> list:
    """
    Загружает список транзакций из JSON-файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []

# пример вызова
transactions = load_transactions('../data/operations.json')
logger.info(f"Загружено {len(transactions)} транзакций")
