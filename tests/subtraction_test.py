"""Testing Subtraction"""
import pytest
import pandas as pd
from calc.calculations.subtraction import Subtraction



@pytest.fixture
def file_name(csv_dir_path):

    with open("datamanager/csv_test_excel/subtraction_1000.csv", 'r') as infile:
        reader = pd.read_csv(infile, delimiter=",")
    return reader


def test_static_calculation_subtraction(subtraction_file_fixture):
    """testing that our calculator has a static method for subtraction"""
    # Assert

    for index, row in subtraction_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        subtraction = Subtraction.create(tuple_values)
        # Assert
        assert subtraction.get_result() == row.result
