def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX
    Показывает первые 6 и последние 4 цифры, остальные заменяет на *
    """
    # Удаляем все пробелы (если есть) и проверяем, что номер состоит из цифр
    clean_number = card_number.replace(" ", "")
    if not clean_number.isdigit():
        raise ValueError("Ошибка: Номер карты должен содержать только цифры")

    # Проверяем длину номера карты (обычно 16 цифр)
    if len(clean_number) != 16:
        raise ValueError("Ошибка: Номер карты должен содержать 16 цифр")

    # Форматируем номер карты по маске
    masked = f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX
    Показывает только последние 4 цифры, перед ними **
    """
    if not isinstance(account_number, str):
        raise AttributeError("Ошибка: Номер счета должен быть строкой")

    # Удаляем все пробелы (если есть) и проверяем, что номер состоит из цифр
    clean_number = account_number.replace(" ", "")
    if not clean_number.isdigit():
        raise ValueError("Ошибка: Номер счета должен содержать только цифры")

    # Проверяем минимальную длину номера счета
    if len(clean_number) < 4:
        raise ValueError("Ошибка: Номер счета должен содержать минимум 4 цифры")

    # Форматируем номер счета по маске
    masked = f"**{clean_number[-4:]}"
    return masked


print(get_mask_card_number("1234569874563215"))
print(get_mask_account("736565156189784564984"))
