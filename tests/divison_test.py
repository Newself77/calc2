"""Testing Division"""
from functools import lru_cache
from os import path
from calc.calculations.division import Division


@lru_cache(None)
def division_file_fixture():
    """Method to pull CSV files"""
    return Division("datamanager/csv_test_excel/division_1000.csv")


def test_static_calculation_division():
    """testing that our calculator has a static method for division"""
    # Assert
    division = division_file_fixture()
    result = division.divide() == division.values['result']
    assert result.all()


def test_bad_division():
    """Testing Bad Division"""
    file = path.join(__file__, "../../datamanager/csv_test_excel/_bad_divide.csv")
    file = path.abspath(path.normpath(file))
    assert Division(file).divide() == []
    assert Division((1, 0)).divide() == float("inf")
