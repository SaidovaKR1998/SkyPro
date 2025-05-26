# def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
#     """
#     Фильтрует список словарей по значению ключа 'state'.
#
#     :param transactions: Список словарей с транзакциями
#     :param state: Значение состояния для фильтрации (по умолчанию 'EXECUTED')
#     :return: Отфильтрованный список словарей
#     """
#     return [transaction for transaction in transactions if transaction.get("state") == state]
#
# def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
#     """
#     Сортирует список словарей по дате (ключ 'date').
#
#     :param transactions: Список словарей с транзакциями
#     :param reverse: Флаг сортировки (по умолчанию True - по убыванию)
#     :return: Отсортированный список словарей
#     """
#     return sorted(
#         transactions,
#         key=lambda x: x["date"],
#         reverse=reverse
#     )
#
# def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
#     """
#     Фильтрует список словарей по значению ключа 'state'.
#
#     :param transactions: Список словарей с транзакциями
#     :param state: Значение состояния для фильтрации (по умолчанию 'EXECUTED')
#     :return: Отфильтрованный список словарей
#     """
#     return [transaction for transaction in transactions if transaction.get("state") == state]
#
# def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
#     """
#     Сортирует список словарей по дате (ключ 'date').
#
#     :param transactions: Список словарей с транзакциями
#     :param reverse: Флаг сортировки (по умолчанию True - по убыванию)
#     :return: Отсортированный список словарей
#     """
#     return sorted(
#         transactions,
#         key=lambda x: x["date"],
#         reverse=reverse
#     )
#
# transactions = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
# ]
#
# print(filter_by_state(transactions))
# print(sort_by_date(transactions))
def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями
    :param state: Значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список словарей
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате (ключ 'date').

    :param transactions: Список словарей с транзакциями
    :param reverse: Флаг сортировки (по умолчанию True - по убыванию)
    :return: Отсортированный список словарей
    """
    return sorted(
        transactions,
        key=lambda x: x["date"],
        reverse=reverse
    )


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]


print(filter_by_state(transactions))
print(sort_by_date(transactions))
