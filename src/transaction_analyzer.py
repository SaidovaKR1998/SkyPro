import re  # Импортируем модуль для работы с регулярными выражениями
from typing import List, Dict  # Это для подсказок типов (не обязательно, но полезно)

# Наша первая функция - фильтрация транзакций по описанию
def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует транзакции, оставляя только те, где в описании есть искомая строка
    :param transactions: Список транзакций (каждая транзакция - словарь)
    :param search_string: Строка для поиска в описании
    :return: Отфильтрованный список транзакций
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Создаем шаблон поиска без учета регистра
    return [tx for tx in transactions if pattern.search(tx.get('description', ''))]  # Ищем в каждом описании

# Функция подсчета операций по категориям
def count_transactions_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Считает сколько транзакций относится к каждой категории
    :param transactions: Список транзакций
    :param categories: Список категорий для поиска
    :return: Словарь {категория: количество}
    """
    result = {category: 0 for category in categories}  # Создаем словарь с нулями

    for tx in transactions:  # Перебираем все транзакции
        description = tx.get('description', '').lower()  # Описание в нижнем регистре
        for category in categories:  # Проверяем каждую категорию
            if category.lower() in description:  # Если категория есть в описании
                result[category] += 1  # Увеличиваем счетчик
                break  # Переходим к следующей транзакции

    return result

# Основная функция main()
def main():
    # Приветствие
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Выбор типа файла
    file_type = input("> ")

    file_types = {
        '1': 'JSON',
        '2': 'CSV',
        '3': 'XLSX'
    }

    if file_type not in file_types:
        print("Неверный выбор файла.")
        return

    print(f"Для обработки выбран {file_types[file_type]}-файл.")

# Фильтрация по статусу операции
    # Создаем тестовые данные (в реальной программе будем загружать из файла)
    transactions = [
        {
            'date': '08.12.2019',
            'description': 'Открытие вклада',
            'from': 'Счет 12344321',
            'to': 'Счет 4321',
            'amount': '40542',
            'currency': 'руб.',
            'status': 'EXECUTED'
        },
        # ... другие транзакции ...
    ]

    # Фильтрация по статусу
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:  # Бесконечный цикл, пока не получим правильный статус
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status = input("> ").upper()  # Переводим в верхний регистр

        if status in valid_statuses:
            break  # Выходим из цикла если статус правильный
        print(f'Статус операции "{status}" недоступен.')

    # Фильтруем транзакции
    filtered_transactions = [tx for tx in transactions if tx.get('status', '').upper() == status]
    print(f'Операции отфильтрованы по статусу "{status}"')

# Дополнительные фильтры
    # Сортировка по дате
    sort_date = input("Отсортировать операции по дате? Да/Нет\n> ").lower()
    if sort_date in ['да', 'д', 'yes', 'y']:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n> ").lower()
        reverse = sort_order in ['по убыванию', 'убыванию', 'убывание', 'desc']
        filtered_transactions.sort(key=lambda x: x['date'], reverse=reverse)

    # Фильтрация по валюте (только рубли)
    rub_only = input("Выводить только рублевые транзакции? Да/Нет\n> ").lower()
    if rub_only in ['да', 'д', 'yes', 'y']:
        filtered_transactions = [tx for tx in filtered_transactions
                                 if tx.get('currency', '').lower() in ['руб.', 'rub', 'rur']]

    # Фильтрация по ключевому слову
    filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n> ").lower()
    if filter_word in ['да', 'д', 'yes', 'y']:
        search_word = input("Введите слово для поиска в описании:\n> ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_word)

# Вывод результата
    # Вывод результатов
    print("Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}\n")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    for tx in filtered_transactions:
        print(f"{tx['date']} {tx['description']}")

        # Маскировка номера счета/карты отправителя
        from_account = tx.get('from', '')
        if from_account:
            if 'счет' in from_account.lower():
                parts = from_account.split()
                last_four = parts[-1][-4:]
                print(f"Счет **{last_four}", end="")
            else:
                # Маскировка номера карты (например: 4276 54** **** 1234)
                card_parts = from_account.split()
                card_number = card_parts[-1]
                masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                print(f"{' '.join(card_parts[:-1])} {masked}", end="")

            print(" -> ", end="")

        # Маскировка номера счета/карты получателя
        to_account = tx.get('to', '')
        if 'счет' in to_account.lower():
            parts = to_account.split()
            last_four = parts[-1][-4:]
            print(f"Счет **{last_four}")
        else:
            card_parts = to_account.split()
            card_number = card_parts[-1]
            masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            print(f"{' '.join(card_parts[:-1])} {masked}")

        print(f"Сумма: {tx['amount']} {tx['currency']}\n")

# Запуск программы
if __name__ == "__main__":
    main()
