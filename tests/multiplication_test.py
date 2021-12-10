"""Testing Multiplication"""
from functools import lru_cache
from os import path
from calc.calculations.multiplication import Multiplication


@lru_cache(None)
def multiplication_file_fixture():
    """Method to pull CSV files"""
    return Multiplication("datamanager/csv_test_excel/multiplication_1000.csv")


def test_static_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    # Assert
    multiplication = multiplication_file_fixture()
    result = multiplication.multiply() == multiplication.values['result']
    assert result.all()


def test_bad_multiply():
    """Testing Bad Multiplication"""
    file = path.join(__file__, "../../datamanager/csv_test_excel/_bad_multiply.csv")
    file = path.abspath(path.normpath(file))
    assert Multiplication(file).multiply() == []
