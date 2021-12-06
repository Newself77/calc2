"""Testing Addition"""

import pytest
import pandas as pd
from calc.calculations.addition import Addition



@pytest.fixture
def file_name(csv_dir_path):
    """Method to pull CSV files"""
    with open("datamanager/csv_test_excel/add_1000.csv", 'r') as infile:
        reader = pd.read_csv(infile, delimiter=",")
    return reader


def test_static_calculation_addition(addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    # Assert

    for index, row in addition_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        addition = Addition.create(tuple_values)
        # Assert
        assert addition.get_result() == row.result
