import pytest
from operators import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(1, 0) == 1
    assert add(0, 1) == 1
    assert add(1.5, 2.25) == pytest.approx(3.75)

def test_subtract():
    assert subtract(2, 4) == -2
    assert subtract(5, 2) ==  3
    assert subtract(0, 1) == -1
    assert subtract(1, 0) ==  1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(3, 0) == 0
    assert multiply(3, 1) == 3
    assert multiply(1, 3) == 3

def test_divide():
    assert divide(8, 2) == 4
    assert divide(0, 2) == 0
    assert divide(2, 1) == 2
    assert divide(7, 2) == pytest.approx(3.25)
    assert divide(9,   -2) == pytest.approx(-4.5)

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
