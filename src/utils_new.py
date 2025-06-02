import json
import pandas as pd
from pathlib import Path
from typing import Union, List, Dict
from src.log_config import logger


def load_transactions(file_path: Union[str, Path]) -> List[Dict]:
    """
    Загружает список транзакций из файла (JSON, CSV или XLSX).

    Args:
        file_path: Путь к файлу с транзакциями

    Returns:
        Список словарей с данными о транзакциях. Если файл не найден, пустой или
        имеет неподдерживаемый формат, возвращается пустой список.
    """
    try:
        file_path = Path(file_path)
        if not file_path.exists():
            logger.error(f"Файл не найден: {file_path}")
            return []

        if file_path.suffix.lower() == '.json':
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    logger.warning(f"Данные в JSON-файле {file_path} не являются списком")
                    return []

        elif file_path.suffix.lower() == '.csv':
            data = pd.read_csv(file_path).to_dict('records')

        elif file_path.suffix.lower() in ('.xlsx', '.xls'):
            data = pd.read_excel(file_path).to_dict('records')

        else:
            logger.error(f"Неподдерживаемый формат файла: {file_path}")
            return []

        logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
        return data

    except Exception as e:
        logger.error(f"Ошибка при загрузке файла {file_path}: {str(e)}")
        return []


# Примеры вызова
json_transactions = load_transactions('../data/operations.json')
csv_transactions = load_transactions('../data/operations.csv')
xlsx_transactions = load_transactions('../data/operations.xlsx')

logger.info(f"Загружено {len(json_transactions)} JSON транзакций")
logger.info(f"Загружено {len(csv_transactions)} CSV транзакций")
logger.info(f"Загружено {len(xlsx_transactions)} XLSX транзакций")
