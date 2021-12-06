"""Testing Division"""
from calc.calculations.division import Division


def test_static_calculation_division(division_file_fixture):
    """testing that our calculator has a static method for division"""
    # Assert
    for index, row in division_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        division = Division.create(tuple_values)
        # Assert
        assert division.get_result() == row.result
