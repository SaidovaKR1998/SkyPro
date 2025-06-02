import unittest
from src.transaction_analyzer import filter_transactions_by_description, count_transactions_by_categories

# Тестовые данные
TEST_TRANSACTIONS = [
    {
        'description': 'Перевод организации',
        'status': 'EXECUTED',
        'date': '2023-01-01',
        'currency': 'руб.'
    },
    {
        'description': 'Открытие вклада',
        'status': 'EXECUTED',
        'date': '2023-01-02',
        'currency': 'USD'
    },
    {
        'description': 'Перевод с карты на карту',
        'status': 'CANCELED',
        'date': '2023-01-03',
        'currency': 'EUR'
    },
    {
        'description': 'Оплата услуг',
        'status': 'PENDING',
        'date': '2023-01-04',
        'currency': 'руб.'
    }
]


class TestTransactionFunctions(unittest.TestCase):

    def test_filter_by_description(self):
        """Тест фильтрации по описанию"""
        # Поиск по слову "перевод" (должно найти 2 транзакции)
        result = filter_transactions_by_description(TEST_TRANSACTIONS, 'перевод')
        self.assertEqual(len(result), 2)

        # Поиск по слову "вклад" (должно найти 1 транзакцию)
        result = filter_transactions_by_description(TEST_TRANSACTIONS, 'вклад')
        self.assertEqual(len(result), 1)

        # Поиск без учета регистра
        result = filter_transactions_by_description(TEST_TRANSACTIONS, 'ПЕРЕВОД')
        self.assertEqual(len(result), 2)

        # Поиск несуществующего слова
        result = filter_transactions_by_description(TEST_TRANSACTIONS, 'кредит')
        self.assertEqual(len(result), 0)

    def test_count_by_categories(self):
        """Тест подсчета по категориям (с учётом нового поведения Counter)"""
        categories = ['перевод', 'вклад', 'оплата']

        # Ожидаемый результат: {'перевод': 2, 'вклад': 1, 'оплата': 1}
        result = count_transactions_by_categories(TEST_TRANSACTIONS, categories)

        self.assertEqual(result['перевод'], 2)
        self.assertEqual(result['вклад'], 1)
        self.assertEqual(result['оплата'], 1)

        # Проверка несуществующей категории (должна вернуть 0)
        categories = ['кредит']
        result = count_transactions_by_categories(TEST_TRANSACTIONS, categories)
        self.assertEqual(result['кредит'], 0)

        # Проверка регистронезависимости (если категория передана в верхнем регистре)
        categories = ['ПЕРЕВОД', 'ВКЛАД']
        result = count_transactions_by_categories(TEST_TRANSACTIONS, categories)
        self.assertEqual(result['ПЕРЕВОД'], 2)  # Счётчик должен работать
        self.assertEqual(result['ВКЛАД'], 1)


if __name__ == '__main__':
    unittest.main()
