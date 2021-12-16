"""Testing Calculation"""
import pytest
from calc.calculations.calculation import Calculation

def test_bad_filename():
    """Testing Bad Filename"""
    with pytest.raises(ValueError):
        Calculation("Bad_File")

def test_added_filename():
    """Testing a secondary filename"""
    calculation = Calculation([2, 4], "MyTest.csv")
    assert calculation.filename == "MyTest.csv"

