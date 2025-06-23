import pytest
from calculator_cli.calculator import (
    add, subtract, multiply, divide,
    power, modulus, square_root
)

def test_add():
    assert add(1, 2, 3) == 6
    assert add() == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(100, 30, 20) == 50

def test_multiply():
    assert multiply(2, 3, 4) == 24
    assert multiply(1) == 1

def test_divide():
    assert divide(100, 2) == 50
    assert divide(100, 2, 5) == 10
    with pytest.raises(ValueError):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(100, 10) == 0

def test_square_root():
    assert square_root(25) == 5
    with pytest.raises(ValueError):
        square_root(-4)
