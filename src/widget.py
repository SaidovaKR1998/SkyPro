def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в переданной строке.

    :param account_info: Строка с названием и номером карты/счета (например, "Visa Platinum 7000792289606361")
    :return: Строка с маскированным номером (например, "Visa Platinum 7000 79** **** 6361")
    """
    if not account_info:
        return ""

    # Разделяем строку на название и номер
    parts = account_info.rsplit(' ', 1)
    if len(parts) != 2:
        return account_info  # если не удалось разделить (нет номера)

    name, number = parts

    # Оставляем только цифры в номере
    digits = ''.join(filter(str.isdigit, number))

    if 16 <= len(digits) <= 19:  # Номер карты (16-19 цифр)
        masked_number = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    elif len(digits) == 20:  # Номер счета
        masked_number = f"**{digits[-4:]}"
    else:  # Неизвестный формат
        return account_info

    return f"{name} {masked_number}"


def get_date(iso_date: str) -> str:
    """
    Преобразует дату из формата ISO в формат 'ДД.ММ.ГГГГ'

    :param iso_date: Строка с датой в формате "2024-03-11T02:26:18.671407"
    :return: Строка с датой в формате "11.03.2024"
    """
    try:
        # Разделяем дату и время
        date_part = iso_date.split('T')[0]
        year, month, day = date_part.split('-')
        return f"{day}.{month}.{year}"
    except (IndexError, ValueError):
        return ""


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("МИР 1234567890123456"))

print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2023-12-31T23:59:59.999999"))
print(get_date("2020-02-29T00:00:00.000000"))
