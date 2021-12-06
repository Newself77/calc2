"""Testing Division"""
import pytest

import pandas as pd

from calc.calculations.division import Division


@pytest.fixture
def read_file(csv_dir_path):
    """method for pull csv file"""
    with open("datamanager/csv_test_excel/division_1000.csv", 'r') as infile:
        reader = pd.read_csv(infile, delimiter=",")
    return reader


def test_static_calculation_division(division_file_fixture):
    """testing that our calculator has a static method for division"""
    # Assert

    for index, row in division_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        division = Division(tuple_values)
        # Assert
        assert division.get_result() == row.result