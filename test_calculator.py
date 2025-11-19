# https://github.com/DomanMahler/lab11-GD-DM
# Partner 1: Gavin DeYoung
# Partner 2: Doman Mahler

import pytest
import math
import calculator

#Partner 2 tests

def test_add():
    assert calculator.add(5, 3) == 8

def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(0, 10)

def test_logarithm():
    result = calculator.logarithm(8, 2)
    assert math.isclose(result, 3.0, rel_tol=1e-9)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        calculator.logarithm(10, -1)


#Partner 1 tests

def test_multiply():
    assert calculator.multiply(3, 4) == 12

def test_divide():
    assert calculator.divide(2, 10) == 5

def test_log_invalid_argument():
    with pytest.raises(ValueError):
        calculator.logarithm(-5, 2)

def test_hypotenuse():
    result = calculator.hypotenuse(3, 4)
    assert math.isclose(result, 5.0, rel_tol=1e-9)

def test_sqrt():
    result = calculator.square_root(16)
    assert result == 4