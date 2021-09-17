from Fizz import fizzbuzz
import pytest

@pytest.mark.parametrize("test_input, expected", [(3, "Fizz"), (6, "Fizz"), (9, "Fizz"), (12, "Fizz")])
def test_debeImprimirFizzEnMultiplosDe3(test_input, expected):
    assert fizzbuzz(test_input) == expected
