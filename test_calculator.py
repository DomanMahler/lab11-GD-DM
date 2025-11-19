# https://github.com/DomanMahler/lab11-GD-DM
# Partner 1: Gavin DeYoung
# Partner 2: Doman Mahler
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
         self.assertEqual(calculator.subtract(10, 4), 6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(8, 2), 3.0, places=6)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -1)

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-5, 2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0, places=6)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4)


if __name__ == '__main__':
    unittest.main()