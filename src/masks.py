from src.log_config import logger

def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX
    Показывает первые 6 и последние 4 цифры, остальные заменяет на *
    """
    try:
        # Удаляем все пробелы (если есть) и проверяем, что номер состоит из цифр
        clean_number = card_number.replace(" ", "")
        if not clean_number.isdigit():
            raise ValueError("Номер карты должен содержать только цифры")
        # Проверяем длину номера карты (обычно 16 цифр)
        if len(clean_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")
        # Форматируем номер карты по маске
        masked = f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"
        logger.info(f"Маскирован номер карты: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")
        raise

def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX
    Показывает только последние 4 цифры, перед ними **
    """
    try:
        if not isinstance(account_number, str):
            raise AttributeError("Номер счета должен быть строкой")
        clean_number = account_number.replace(" ", "")
        if not clean_number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")
        if len(clean_number) < 4:
            raise ValueError("Номер счета должен содержать минимум 4 цифры")
        masked = f"**{clean_number[-4:]}"
        logger.info(f"Маскирован номер счета: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счета: {e}")
        raise

# тестовые вызовы
print(get_mask_card_number("1234569874563215"))
print(get_mask_account("736565156189784564984"))
