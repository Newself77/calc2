"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication


def test_static_calculation_multiplication(multiplication_file_fixture):
    """testing that our calculator has a static method for addition"""
    # Assert
    for index, row in multiplication_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        # Act
        multiplication = Multiplication.create(tuple_values)
        # Assert
        assert multiplication.get_result() == row.result
