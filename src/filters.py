"""Модуль функциональной фильтрации списков."""

from typing import Iterable, List


def filter_even_numbers(numbers: Iterable[int]) -> List[int]:
    """Фильтрует только чётные числа из переданной последовательности.

    Использует встроенную функцию высшего порядка filter и lambda-выражение.

    Параметры:
        numbers (Iterable[int]): Исходная числовая последовательность.

    Возвращает:
        List[int]: Новый список, содержащий только чётные числа.
    """
    for item in numbers:
        if not isinstance(item, int):
            raise TypeError(
                f"Элементы должны быть целыми числами, получено: {type(item).__name__}"
            )

    return list(filter(lambda x: x % 2 == 0, numbers))
