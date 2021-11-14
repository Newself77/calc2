"""Testing the Calculator"""
from calculator.calculator import Calculator


def test_calculator_add():
    """Testing the Add function of calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6


def test_calculator_subtract():
    """Testing the subtract function of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1


def test_calculator_multiply():
    """Tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2
