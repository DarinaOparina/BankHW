#Виджет банковских операций клиента

##Установка

 **Клонируйте репозиторий** на свой компьютер:
 ```https://github.com/DarinaOparina/BankHW.git```

 ##Реализованные функции:

 1. get_mask_card_number
 Маскирует номер банковской карты
2. get_mask_account
 Маскирует номер банковского счёта
3. filter_by_state
 Фильтрует список словарей по значению ключа 'state'
4. sort_by_date
 Сортирует список словарей по ключу 'date'
5. mask_account_card
 Маскирует номер карты или счёта
6. get_data
 Преобразует строку с датой в формат ДД.ММ.ГГГГ.

##Настройки линтеров

### Настройка mypy
Создайте файл `mypy` в корне проекта и добавьте:
```
[mypy]
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

### Настройка flake8
Создайте файл `.flake8` в корне проекта и добавьте:
```
[flake8]
max-line-length = 88
extend-ignore = E203
exclude = .git,__pycache__,build,dist,.venv,venv
```