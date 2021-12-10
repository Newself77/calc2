"""Testing Subtraction"""
from functools import lru_cache
from os import path
from calc.calculations.subtraction import Subtraction


@lru_cache(None)
def subtraction_file_fixture():
    """Creates Subtraction object"""
    return Subtraction("datamanager/csv_test_excel/subtraction_1000.csv")


def test_static_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    # Assert
    subtraction = subtraction_file_fixture()
    result = subtraction.subtract() == subtraction.values['result']
    assert result.all()


def test_bad_subtract():
    """Testing Bad Subtraction"""
    file = path.join(__file__, "../../datamanager/csv_test_excel/_bad_subtract.csv")
    file = path.abspath(path.normpath(file))
    assert Subtraction(file).subtract() == []
