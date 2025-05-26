# logger_config.py
import logging
import os

# Получить текущую директорию (например, src)
current_dir = os.getcwd()

# Подняться на уровень выше (до SkyPro)
project_root = os.path.dirname(current_dir)

# Путь к папке logs
logs_dir = os.path.join(project_root, 'logs')

# Создать папку logs, если не существует
os.makedirs(logs_dir, exist_ok=True)

# Настройка форматирования
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Создаем хранилище логгера
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # или другой уровень по необходимости

# Создаем обработчик для записи в файл (перезаписывать при каждом запуске)
file_handler = logging.FileHandler(os.path.join(logs_dir, 'application.log'), mode='w', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(log_format))

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)
