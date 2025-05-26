import logging
import os
from pathlib import Path


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """Настройка логгера для модуля"""

    # Создаем папку logs если ее нет
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Формат сообщений
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Обработчик для записи в файл (перезаписывает файл при каждом запуске)
    file_handler = logging.FileHandler(
        filename=logs_dir / log_file,
        mode='w'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
