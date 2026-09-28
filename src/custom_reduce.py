"""Модуль собственной реализации функции свертки reduce."""

from typing import Callable, Iterable, TypeVar, Any

T = TypeVar("T")
_MISSING = object()


def custom_reduce(
    function: Callable[[Any, Any], Any],
    iterable: Iterable[T],
    initial: Any = _MISSING
) -> Any:
    """Последовательно сворачивает элементы коллекции с помощью бинарной функции.

    Полностью воспроизводит стандартную семантику functools.reduce.

    Параметры:
        function (Callable): Функция двух аргументов.
        iterable (Iterable): Сворачиваемая последовательность.
        initial (Any): Опциональное начальное значение аккумулятора.

    Возвращает:
        Any: Итоговое аккумулированное значение.
    """
    it = iter(iterable)
    if initial is _MISSING:
        try:
            accumulator = next(it)
        except StopIteration:
            raise TypeError(
                "custom_reduce() of empty iterable with no initial value"
            )
    else:
        accumulator = initial

    for element in it:
        accumulator = function(accumulator, element)

    return accumulator
