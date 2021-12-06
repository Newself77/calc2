"""Testing Multiplication"""
import pytest
import pandas as pd
from calc.calculations.multiplication import Multiplication



@pytest.fixture
def read_file(csv_dir_path):
    """Method for csv file to read"""
    with open("datamanager/csv_test_excel/multiplication_1000.csv", 'r') as infile:
        reader = pd.read_csv(infile, delimiter=",")
    return reader


def test_static_calculation_multiplication(multiplication_file_fixture):
    """testing that our calculator has a static method for multiplication"""
    # Assert

    for index, row in multiplication_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        Multiplication.create(tuple_values)
        # Assert
        assert Multiplication.get_result() == row.result
