"""Модуль декораторов высшего порядка."""

import time
import functools
from typing import Callable, Any


def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор для точного замера времени выполнения функции.

    Сохраняет docstring и сигнатуру декорируемой функции с помощью functools.wraps.
    Фиксирует время выполнения в атрибуте `last_execution_time`.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        wrapper.last_execution_time = duration  # type: ignore
        return result

    wrapper.last_execution_time = 0.0  # type: ignore
    return wrapper
