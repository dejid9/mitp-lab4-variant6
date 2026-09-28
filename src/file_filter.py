"""Модуль ленивой потоковой фильтрации файлов через генератор."""

from typing import Iterator, Callable


def filter_file_lines(
    filepath: str,
    predicate: Callable[[str], bool] | None = None,
    keyword: str | None = None
) -> Iterator[str]:
    """Лениво читает строки файла и возвращает только удовлетворяющие условию.

    Использует yield для потоковой обработки без загрузки всего файла в ОЗУ.

    Параметры:
        filepath (str): Путь к текстовому файлу.
        predicate (Callable[[str], bool] | None): Предикат-фильтр.
        keyword (str | None): Опциональное ключевое слово для поиска.

    Выдаёт:
        Iterator[str]: Строки файла, прошедшие фильтрацию (без завершающего \n).
    """
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.rstrip("\r\n")
            if keyword is not None and keyword not in clean_line:
                continue
            if predicate is not None and not predicate(clean_line):
                continue
            yield clean_line
