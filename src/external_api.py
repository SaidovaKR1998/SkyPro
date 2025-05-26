import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма в рублях (float)
    """
    try:
        # Получаем сумму и валюту
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        # Если уже рубли - возвращаем как есть
        if currency == 'RUB':
            return amount

        # Конвертируем USD/EUR в RUB
        if currency in ('USD', 'EUR'):
            rate = get_exchange_rate(currency)
            if rate:
                return round(amount * rate, 2)
            return 0.0

        # Для других валют возвращаем 0 (или можно добавить обработку)
        return 0.0

    except (KeyError, ValueError):
        return 0.0


def get_exchange_rate(currency: str) -> float:
    """
    Получает курс валюты к рублю через API.

    Args:
        currency: Код валюты (USD, EUR)

    Returns:
        Курс валюты к рублю или None при ошибке
    """
    try:
        response = requests.get(
            f"{BASE_URL}/latest",
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY},
            timeout=5
        )
        response.raise_for_status()
        return response.json()['rates']['RUB']
    except Exception as e:
        print(f"Ошибка при получении курса: {e}")
        return None
