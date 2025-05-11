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

3. В пакете **tests** созданы 4 файла с тестами:
- **test_widget.py** - модуль содержит тесты для функций *mask_account_card* и *get_date*
- **test_masks.py** - модуль содержит тесты для функций *get_mask_card_number* и *get_date*
- **test_processing.py** - модуль содержит тесты для функций *filter_by_state* и *sort_by_date*
- **test_generators.py** - модуль содержит тесты для функций *filter_by_currency* *transaction_descriptions* и *card_number_generator*

Функциональный код покрыт тестами более чем на 80%. В репозитории есть папка с отчетом покрытия тестами в формате HTML.

**Установка**
1. Клонируйте репозиторий:
- HTTPS https://github.com/SaidovaKR1998/SkyPro.git
- SHH git@github.com:SaidovaKR1998/SkyPro.git