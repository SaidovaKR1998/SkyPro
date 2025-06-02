# SkyPro

**Описание**
- SkyPro - это проект над которым работаю во время учебы, выполняю домашние работы


1. Создан файл *.gitignore* в корне проекта и добавлены в него стандартные шаблоны для Python, чтобы исключить системные и временные файлы, такие как 
*pycache*, *.idea* и другие. 

2. В пакете **src** созданы модули:
- **widget.py** - модуль содержит функции *mask_account_card* и *get_date*
- **masks.py** - модуль содержит функции *get_mask_card_number* и *get_date*
- **processing.py** - модуль содержит функции *filter_by_state* и *sort_by_date*
- **generators.py** - модуль содержит функции *filter_by_currency* *transaction_descriptions* и *card_number_generator*
- **decorators.py** - модуль содержит декоратор *log*
- **external_api.py** - модуль содержит функции *convert_to_rub* и *get_exchange_rate*
- **utils.py** - модуль содержит функцию *load_transactions* (поддержка только JSON-файла)
- **utils_new.py** - модуль содержит функцию *load_transactions* (поддержка JSON-, CSV- и XLSX-файлов)
- **transaction_analyzer.py** - модуль содержит функции *filter_transactions_by_description* *count_transactions_by_categories* и *main*

3. В пакете **tests** созданы 5 файлов с тестами:
- **test_widget.py** - модуль содержит тесты для функций *mask_account_card* и *get_date*
- **test_masks.py** - модуль содержит тесты для функций *get_mask_card_number* и *get_date*
- **test_processing.py** - модуль содержит тесты для функций *filter_by_state* и *sort_by_date*
- **test_generators.py** - модуль содержит тесты для функций *filter_by_currency* *transaction_descriptions* и *card_number_generator*
- **test_log_decorator.py** - модуль содержит тесты для декоратора *log* из модуля *decorators*
- **test_external_api.py** - модуль содержит тесты для функций *convert_to_rub* и *get_exchange_rate*
- **test_utils.py** - модуль содержит тесты для функции *load_transactions* (поддержка только JSON-файла)
- **test_utils_new.py** - модуль содержит тесты для функции *load_transactions* (поддержка JSON-, CSV- и XLSX-файлов)
- **test_transaction_analyzer.py** - модуль содержит тесты для функций *filter_transactions_by_description* *count_transactions_by_categories* и *main*

Функциональный код покрыт тестами более чем на 80%. В репозитории есть папка с отчетом покрытия тестами в формате HTML.

**Установка**
1. Клонируйте репозиторий:
- HTTPS https://github.com/SaidovaKR1998/SkyPro.git
- SHH git@github.com:SaidovaKR1998/SkyPro.git