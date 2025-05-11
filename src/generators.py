def filter_by_currency(transactions, currency_code):
    """
    Функция filter_by_currency, которая принимает список транзакций и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """
    Генератор transaction_descriptions, который принимает список словарей с
    транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start, end):
    """
    Генератор card_number_generator, который генерирует номера банковских карт в
    указанном диапазоне в формате XXXX XXXX XXXX XXXX.
    """
    for num in range(start, end + 1):
        # Форматируем число в 16-значную строку с ведущими нулями
        card_num = f"{num:016d}"
        # Разбиваем на группы по 4 цифры и объединяем через пробел
        formatted_num = ' '.join([card_num[i:i+4] for i in range(0, 16, 4)])
        yield formatted_num

for card_number in card_number_generator(1, 5):
    print(card_number)