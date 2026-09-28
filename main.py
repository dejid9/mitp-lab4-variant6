"""Главный модуль демонстрации решений лабораторной работы №4 (Вариант 6)."""

import os
from src.filters import filter_even_numbers
from src.prime_generator import prime_generator
from src.decorators import timeit
from src.file_filter import filter_file_lines
from src.custom_reduce import custom_reduce


@timeit
def compute_heavy_task(n: int) -> int:
    """Выполняет демонстрационное вычисление с замером времени."""
    return sum(i * i for i in range(n))


def main() -> None:
    print("=" * 65)
    print("Лабораторная работа №4 — Вариант 6")
    print("Дисциплина: «Методы и технологии программирования»")
    print("Студент: Вафин Денис Наильевич (Группа 221141)")
    print("=" * 65)

    # 1. Задание 2 (среднее): Фильтрация чётных чисел
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22]
    evens = filter_even_numbers(numbers)
    print("\n[1] Фильтрация чётных чисел (filter + lambda):")
    print(f"    Исходный список: {numbers}")
    print(f"    Чётные числа:    {evens}")

    # 2. Задание 6 (среднее): Генератор простых чисел
    limit = 35
    primes = list(prime_generator(limit=limit))
    print(f"\n[2] Генератор простых чисел до {limit} (yield):")
    print(f"    Простые числа: {primes}")

    # 3. Задание 8 (среднее): Декоратор замера времени @timeit
    print("\n[3] Декоратор замера времени работы функции (@timeit):")
    res = compute_heavy_task(300_000)
    elapsed = getattr(compute_heavy_task, "last_execution_time", 0.0)
    print(f"    Результат вычислений: {res}")
    print(f"    Зафиксированное время: {elapsed:.6f} сек.")

    # 4. Задание 4 (повышенное): Фильтрация данных из файла через генератор
    log_path = os.path.join("data", "server_logs.txt")
    print(f"\n[4] Потоковая фильтрация файла через генератор ({log_path}):")
    error_lines = list(filter_file_lines(log_path, keyword="ERROR"))
    for idx, line in enumerate(error_lines, 1):
        print(f"    [{idx}] {line}")

    # 5. Задание 10 (повышенное): Собственный reduce
    nums = [1, 2, 3, 4, 5]
    total_sum = custom_reduce(lambda x, y: x + y, nums, 0)
    total_prod = custom_reduce(lambda x, y: x * y, nums, 1)
    max_val = custom_reduce(lambda x, y: x if x > y else y, nums)
    print("\n[5] Собственная реализация функции свертки custom_reduce:")
    print(f"    Коллекция: {nums}")
    print(f"    Сумма (reduce +):       {total_sum}")
    print(f"    Произведение (reduce *): {total_prod}")
    print(f"    Максимум (reduce max):   {max_val}")
    print("=" * 65)


if __name__ == "__main__":
    main()
