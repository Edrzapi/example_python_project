
from main.class_file import Calculator

import unittest

class TestCalculatorTheUnitTestWay(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # -------------------------
    # ADDITION
    # -------------------------

    def test_add_two_positive_int_return_positive_int(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_two_negative_int_return_negative_int(self):
        result = self.calc.add(-1, -2)
        self.assertEqual(result, -3)

    def test_add_positive_and_negative_int(self):
        result = self.calc.add(5, -2)
        self.assertEqual(result, 3)

    def test_add_zero(self):
        result = self.calc.add(5, 0)
        self.assertEqual(result, 5)

    # -------------------------
    # SUBTRACTION
    # -------------------------

    def test_sub_two_positive_ints(self):
        result = self.calc.sub(5, 2)
        self.assertEqual(result, 3)

    def test_sub_returns_negative(self):
        result = self.calc.sub(2, 5)
        self.assertEqual(result, -3)

    def test_sub_two_negative_ints(self):
        result = self.calc.sub(-5, -2)
        self.assertEqual(result, -3)

    def test_sub_zero(self):
        result = self.calc.sub(5, 0)
        self.assertEqual(result, 5)

    # -------------------------
    # MULTIPLICATION
    # -------------------------

    def test_mul_two_positive_ints(self):
        result = self.calc.mul(3, 4)
        self.assertEqual(result, 12)

    def test_mul_positive_and_negative_returns_negative(self):
        result = self.calc.mul(3, -4)
        self.assertEqual(result, -12)

    def test_mul_two_negative_returns_positive(self):
        result = self.calc.mul(-3, -4)
        self.assertEqual(result, 12)

    def test_mul_by_zero(self):
        result = self.calc.mul(5, 0)
        self.assertEqual(result, 0)

    # -------------------------
    # DIVISION
    # -------------------------

    def test_div_two_positive_ints(self):
        result = self.calc.div(10, 2)
        self.assertEqual(result, 5)

    def test_div_positive_by_negative_returns_negative(self):
        result = self.calc.div(10, -2)
        self.assertEqual(result, -5)

    def test_div_negative_by_positive_returns_negative(self):
        result = self.calc.div(-10, 2)
        self.assertEqual(result, -5)

    def test_div_two_negative_returns_positive(self):
        result = self.calc.div(-10, -2)
        self.assertEqual(result, 5)

    def test_div_zero_by_number_returns_zero(self):
        result = self.calc.div(0, 5)
        self.assertEqual(result, 0)

    def test_div_by_zero_returns_zero_div_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(5, 0)


if __name__ == "__main__":
    unittest.main()

