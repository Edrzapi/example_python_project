import pytest 
import unittest

@pytest.fixture
def calculator():
    return calculator

def test_add_two_positive_int_return_positive_int():
    assert add(1,2) == 3

# if y == 0: 
#     raise ZeroDivisionError
def test_div_by_zero_returns_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        div(5,0) == 0


class TestCalculatorTheUnitTestWay(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_two_positive_int_return_positive_int(self):
        # Arrange
        self.calc
        # Act
        res= self.calc.add(1,2)
        # Assert
        self.assertEquals(res)

    def test_div_by_zero_returns_zero_div_error(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)


    def tearDown(self):
        self.calc.clear()

