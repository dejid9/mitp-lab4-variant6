"""Модуль, реализующий генератор простых чисел с использованием yield."""

from typing import Iterator


def prime_generator(limit: int | None = None) -> Iterator[int]:
    """Генератор простых чисел, возвращающий простые числа до limit включительно.

    Если limit не указан, генератор является потенциально бесконечным.

    Параметры:
        limit (int | None): Верхняя граница значений простых чисел.

    Выдаёт (yields):
        int: Очередное простое число.
    """
    if limit is not None and limit < 2:
        return

    candidate = 2
    while limit is None or candidate <= limit:
        is_prime = True
        for div in range(2, int(candidate ** 0.5) + 1):
            if candidate % div == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
        candidate += 1
