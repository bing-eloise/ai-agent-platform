import pytest
from src.tools.calculator import calculator

def test_add():
    result = calculator("add", 10, 5)
    assert result == 15


def test_multiply():
    result = calculator("multiply", 8, 4)
    assert result == 32


def test_divide():
    result = calculator("divide", 10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator("divide", 10, 0)