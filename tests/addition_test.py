"""Testing Addition"""
from functools import lru_cache
from os import path
import pytest
from calc.calculations.addition import Addition


@lru_cache(None)
def addition_dataframe():
    """Method to pull CSV files"""
    return Addition("datamanager/csv_test_excel/add_1000.csv")

def test_static_calculation_addition():
    """testing that our calculator has a static method for addition"""
    # Assert
    addition = addition_dataframe()
    result = addition.add() == addition.values['result']
    assert result.all()

def test_wrong_calculation():
    """Testing Bad Addition"""
    with pytest.raises(TypeError):
        Addition((1, None))
    file = path.join(__file__, "../../datamanager/csv_test_excel/_bad_add.csv")
    file = path.abspath(path.normpath(file))
    assert Addition(file).add() == []
