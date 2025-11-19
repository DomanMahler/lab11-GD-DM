# https://github.com/DomanMahler/lab11-GD-DM
# Partner 1: Gavin DeYoung
# Partner 2: Doman Mahler

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide with zero divisor.")
    return b / a

def logarithm(a, base):
    if a <= 0 or base <= 0:
        raise ValueError("Logarithm inputs must be positive.")
    return math.log(a, base)

def exp(a, b):
    return a ** b