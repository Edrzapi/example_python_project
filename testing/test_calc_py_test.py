import pytest
from main.class_file import Calculator


@pytest.fixture
def calculator():
    return Calculator()


# -------------------------
# ADDITION
# -------------------------

def test_add_two_positive_int_returns_positive_int(calculator):
    assert calculator.add(1, 2) == 3


def test_add_two_negative_int_returns_negative_int(calculator):
    assert calculator.add(-1, -2) == -3


def test_add_positive_and_negative_int(calculator):
    assert calculator.add(5, -2) == 3


def test_add_zero(calculator):
    assert calculator.add(5, 0) == 5


# -------------------------
# SUBTRACTION
# -------------------------

def test_sub_two_positive_ints(calculator):
    assert calculator.sub(5, 2) == 3


def test_sub_returns_negative(calculator):
    assert calculator.sub(2, 5) == -3


def test_sub_two_negative_ints(calculator):
    assert calculator.sub(-5, -2) == -3


def test_sub_zero(calculator):
    assert calculator.sub(5, 0) == 5


# -------------------------
# MULTIPLICATION
# -------------------------

def test_mul_two_positive_ints(calculator):
    assert calculator.mul(3, 4) == 12


def test_mul_positive_and_negative_returns_negative(calculator):
    assert calculator.mul(3, -4) == -12


def test_mul_two_negative_returns_positive(calculator):
    assert calculator.mul(-3, -4) == 12


def test_mul_by_zero(calculator):
    assert calculator.mul(5, 0) == 0


# -------------------------
# DIVISION
# -------------------------

def test_div_two_positive_ints(calculator):
    assert calculator.div(10, 2) == 5


def test_div_positive_by_negative_returns_negative(calculator):
    assert calculator.div(10, -2) == -5


def test_div_negative_by_positive_returns_negative(calculator):
    assert calculator.div(-10, 2) == -5


def test_div_two_negative_returns_positive(calculator):
    assert calculator.div(-10, -2) == 5


def test_div_zero_by_number_returns_zero(calculator):
    assert calculator.div(0, 5) == 0


def test_div_by_zero_raises_zero_division_error(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.div(5, 0)


