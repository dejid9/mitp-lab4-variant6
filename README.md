# Лабораторная работа №4

ФИО: Вафин Денис Наильевич
Группа: 221141
Вариант: 6
Лабораторная работа: №4

Дисциплина: «Методы и технологии программирования».

## Выполненные практические задания по варианту 6

### Средней сложности
1. **№2 — Отфильтровать чётные числа из списка.** Реализована функция `filter_even_numbers(numbers: Iterable[int]) -> List[int]` (`src/filters.py`) с использованием функционального стиля (встроенная функция высшего порядка `filter` и лямбда-выражение `lambda x: x % 2 == 0`).
2. **№6 — Создать генератор простых чисел.** Реализован генератор `prime_generator(limit: int | None = None) -> Iterator[int]` (`src/prime_generator.py`) с применением ключевого слова `yield`, обеспечивающий ленивую генерацию простых чисел.
3. **№8 — Декоратор замера времени работы функции.** Реализован параметризованный декоратор `@timeit` (`src/decorators.py`) на базе `functools.wraps`, сохраняющий имя и сигнатуру целевой функции и фиксирующий продолжительность её выполнения через `time.perf_counter()`.

### Повышенной сложности
1. **№4 — Реализовать фильтрацию данных из файла через генератор.** Реализован модуль потоковой построчной фильтрации файлов `filter_file_lines` (`src/file_filter.py`), работающий с константной памятью O(1) за счёт генератора `yield` без загрузки файла целиком в ОЗУ.
2. **№10 — Написать собственный reduce.** Реализована функция свёртки `custom_reduce` (`src/custom_reduce.py`), полностью повторяющая семантику и поведение стандартного `functools.reduce`, включая корректную обработку начального значения `initial` и генерацию исключения `TypeError` для пустых последовательностей.

---

## Архитектура проекта

```text
mitp-lab4-variant6/
├── data/
│   └── server_logs.txt       # Демонстрационный файл логов для потокового генератора
├── src/
│   ├── custom_reduce.py      # Задание 10 (повышенное): собственный reduce
│   ├── decorators.py         # Задание 8 (среднее): декоратор замера времени @timeit
│   ├── file_filter.py        # Задание 4 (повышенное): генераторная фильтрация файлов
│   ├── filters.py            # Задание 2 (среднее): фильтрация чётных чисел
│   └── prime_generator.py    # Задание 6 (среднее): генератор простых чисел
├── tests/
│   └── test_lab4.py          # Набор модульных тестов pytest (15 тестов)
├── .flake8                   # Конфигурация линтера flake8
├── .gitattributes            # Нормализация переносов строк (eol=lf)
├── .gitignore                # Игнорируемые артефакты Python
├── main.py                   # Демонстрационный скрипт
├── README.md                 # Документация и отчёт по лабораторной работе
└── requirements.txt          # Зависимости проекта
```

---

## Установка и запуск

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
python -m flake8 .
python -m pytest -v
```

### Linux / macOS (Bash)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
python3 -m flake8 .
python3 -m pytest -v
```

---

## Подтверждение работы (логи выполнения)

### Демонстрация работы `main.py`:
```text
=================================================================
Лабораторная работа №4 — Вариант 6
Дисциплина: «Методы и технологии программирования»
Студент: Вафин Денис Наильевич (Группа 221141)
=================================================================

[1] Фильтрация чётных чисел (filter + lambda):
    Исходный список: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22]
    Чётные числа:    [2, 4, 6, 8, 10, 22]

[2] Генератор простых чисел до 35 (yield):
    Простые числа: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

[3] Декоратор замера времени работы функции (@timeit):
    Результат вычислений: 8999955000050000
    Зафиксированное время: 0.062234 сек.

[4] Потоковая фильтрация файла через генератор (data\server_logs.txt):
    [1] [2026-09-28 10:01:14] ERROR Database timeout on replica #2
    [2] [2026-09-28 10:02:40] ERROR HTTP 500: Internal server error on /api/v1/auth
    [3] [2026-09-28 10:04:12] ERROR Payment gateway unreachable: timeout

[5] Собственная реализация функции свертки custom_reduce:
    Коллекция: [1, 2, 3, 4, 5]
    Сумма (reduce +):       15
    Произведение (reduce *): 120
    Максимум (reduce max):   5
=================================================================
```

### Результат проверки линтером `flake8`:
```text
python -m flake8 .
[OK] Ошибок не обнаружено, код полностью соответствует PEP 8.
```

### Результаты тестирования `pytest -v`:
```text
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.12.6', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'anyio': '4.15.1', 'html': '4.0.2', 'metadata': '3.1.1', 'ordering': '0.6', 'rerunfailures': '16.4', 'xdist': '3.8.0', 'seleniumbase': '4.51.3'}}
rootdir: C:\Users\dejid\Desktop\Учёба\Новая папка\mitp-lab4-variant6
plugins: anyio-4.15.1, html-4.0.2, metadata-3.1.1, ordering-0.6, rerunfailures-16.4, xdist-3.8.0, seleniumbase-4.51.3
collecting ... collected 15 items

tests/test_lab4.py::TestFilterEvenNumbers::test_mixed_numbers PASSED     [  6%]
tests/test_lab4.py::TestFilterEvenNumbers::test_all_odds PASSED          [ 13%]
tests/test_lab4.py::TestFilterEvenNumbers::test_empty PASSED             [ 20%]
tests/test_lab4.py::TestFilterEvenNumbers::test_negative_evens PASSED    [ 26%]
tests/test_lab4.py::TestFilterEvenNumbers::test_invalid_types_raise PASSED [ 33%]
tests/test_lab4.py::TestPrimeGenerator::test_primes_up_to_20 PASSED      [ 40%]
tests/test_lab4.py::TestPrimeGenerator::test_boundary_zero_and_one PASSED [ 46%]
tests/test_lab4.py::TestPrimeGenerator::test_is_generator PASSED         [ 53%]
tests/test_lab4.py::TestTimeitDecorator::test_preserves_metadata PASSED  [ 60%]
tests/test_lab4.py::TestFileFilterGenerator::test_filter_by_keyword PASSED [ 66%]
tests/test_lab4.py::TestFileFilterGenerator::test_filter_by_predicate PASSED [ 73%]
tests/test_lab4.py::TestCustomReduce::test_matches_functools_reduce PASSED [ 80%]
tests/test_lab4.py::TestCustomReduce::test_single_element_no_initial PASSED [ 86%]
tests/test_lab4.py::TestCustomReduce::test_empty_without_initial_raises PASSED [ 93%]
tests/test_lab4.py::TestCustomReduce::test_empty_with_initial PASSED     [100%]

============================= 15 passed in 0.20s ==============================
```

---

## Git Flow и ветвление

В проекте строго соблюдена модель ветвления Git Flow:
- `main` — стабильная ветка релиза;
- `develop` — ветка интеграции разработки;
- `feature/variant6-functional` — функциональная ветка разработки решений;
- Слияния выполнены исключительно через `--no-ff` с информативными сообщениями коммитов;
- Релиз зафиксирован тегом `v1.0.0`.
