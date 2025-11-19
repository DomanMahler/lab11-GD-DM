import unittest



import math
import pytest
import calculator

def test_add():

    assert calculator.add(2, 3) == 5
    # with negatives
    assert calculator.add(-4, 1) == -3
    # with zero
    assert calculator.add(0, 10) == 10


def test_subtract():

    assert calculator.sub(5, 3) == 2
    assert calculator.sub(3, 5) == -2

    assert calculator.sub(7, 0) == 7


def test_divide_by_zero():
    """
    Lab spec: div(a, b) does b / a and raises ZeroDivisionError if a == 0.
    So we set a == 0 and any b.
    """
    with pytest.raises(ZeroDivisionError):
        calculator.div(0, 10)


def test_logarithm():
    """
    log(a, b) = log_a(b)
    Test a known value: log_2(8) = 3.
    """
    result = calculator.log(2, 8)
    assert math.isclose(result, 3.0, rel_tol=1e-9)

def test_log_invalid_base():

    with pytest.raises(ValueError):
        calculator.log(0, 10)

    with pytest.raises(ValueError):
        calculator.log(1, 10)

    with pytest.raises(ValueError):
        calculator.log(2, 0)

if __name__ == "__main__":
    unittest.main()