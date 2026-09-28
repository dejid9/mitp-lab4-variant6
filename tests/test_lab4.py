"""Набор модульных тестов pytest для лабораторной работы №4."""

import pytest
import functools
from src.filters import filter_even_numbers
from src.prime_generator import prime_generator
from src.decorators import timeit
from src.file_filter import filter_file_lines
from src.custom_reduce import custom_reduce


class TestFilterEvenNumbers:
    def test_mixed_numbers(self):
        assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_all_odds(self):
        assert filter_even_numbers([1, 3, 5, 7]) == []

    def test_empty(self):
        assert filter_even_numbers([]) == []

    def test_negative_evens(self):
        assert filter_even_numbers([-4, -3, 0, 2]) == [-4, 0, 2]

    def test_invalid_types_raise(self):
        with pytest.raises(TypeError):
            filter_even_numbers([1, "2", 3])  # type: ignore


class TestPrimeGenerator:
    def test_primes_up_to_20(self):
        primes = list(prime_generator(20))
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_boundary_zero_and_one(self):
        assert list(prime_generator(1)) == []
        assert list(prime_generator(0)) == []

    def test_is_generator(self):
        gen = prime_generator(10)
        assert hasattr(gen, "__iter__")
        assert hasattr(gen, "__next__")
        assert next(gen) == 2
        assert next(gen) == 3


class TestTimeitDecorator:
    def test_preserves_metadata(self):
        @timeit
        def sample_func(a: int) -> int:
            """Docstring example."""
            return a * 2

        assert sample_func.__name__ == "sample_func"
        assert sample_func.__doc__ == "Docstring example."
        assert sample_func(5) == 10
        assert hasattr(sample_func, "last_execution_time")
        assert sample_func.last_execution_time >= 0.0


class TestFileFilterGenerator:
    def test_filter_by_keyword(self, tmp_path):
        f = tmp_path / "test.log"
        content = (
            "INFO line 1\n"
            "ERROR bug found\n"
            "INFO line 2\n"
            "ERROR crash\n"
        )
        f.write_text(content, encoding="utf-8")

        res = list(filter_file_lines(str(f), keyword="ERROR"))
        assert len(res) == 2
        assert res[0] == "ERROR bug found"
        assert res[1] == "ERROR crash"

    def test_filter_by_predicate(self, tmp_path):
        f = tmp_path / "numbers.txt"
        content = "apple\nbanana\napricot\ncherry\n"
        f.write_text(content, encoding="utf-8")

        res = list(
            filter_file_lines(str(f), predicate=lambda line: line.startswith("a"))
        )
        assert res == ["apple", "apricot"]


class TestCustomReduce:
    def test_matches_functools_reduce(self):
        data = [1, 2, 3, 4, 5]
        expected_sum = functools.reduce(lambda x, y: x + y, data)
        assert custom_reduce(lambda x, y: x + y, data) == expected_sum

        expected_mul = functools.reduce(lambda x, y: x * y, data, 10)
        assert custom_reduce(lambda x, y: x * y, data, 10) == expected_mul

    def test_single_element_no_initial(self):
        assert custom_reduce(lambda x, y: x + y, [42]) == 42

    def test_empty_without_initial_raises(self):
        with pytest.raises(TypeError):
            custom_reduce(lambda x, y: x + y, [])

    def test_empty_with_initial(self):
        assert custom_reduce(lambda x, y: x + y, [], 100) == 100
