"""Testing Division"""
from calc.calculations.subtraction import Subtraction


def test_static_calculation_subtraction(subtraction_file_fixture):
    """testing that our calculator has a static method for addition"""
    # Assert
    for index, row in subtraction_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        subtraction = subtraction.create(tuple_values)
        # Assert
        assert subtraction.get_result() == row.result
