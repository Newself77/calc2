"""Testing the Calculator"""
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


# @pytest.fixture
# def setup_addition_calculation_fixture():
#     """define a function that will run each time you pass it to a test, it is called a fixture"""
#     # pylint: disable=redefined-outer-name
#     values = (1, 2)
#     addition = Addition(values)
#     Calculations.add_calculations(addition)


def test_add_calculation_to_history():
    """Testing clear history returns true for success"""
    assert Calculations.count_history() == 0
    addition = Addition((1, 4))
    addition.add()
    Calculations().add_calculations(addition)
    assert Calculations.count_history() == 1


def test_clear_calculation_history():
    """Testing calculation history"""
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True


def test_get_calculation():
    """Testing getting a specific calculation out of the history"""
    multiply = Multiplication((4, 5))
    multiply.multiply()
    Calculations.add_calculations(multiply)
    assert Calculations.get_calculation(0).get_result() == 20


def test_get_calculation_last():
    """Testing getting a specific calculation out of the history"""
    subtract = Subtraction((3, 0))
    subtract.subtract()
    Calculations.add_calculations(subtract)
    assert Calculations.get_last_calculation().get_result() == 3


def test_get_calculation_first():
    """Testing getting a specific calculation out of the history"""
    assert Calculations.get_first_calculation().get_result() == 20


def test_history_count():
    """Testing getting a specific calculation out of the history"""
    division = Division((8, 2))
    division.divide()
    Calculations.add_calculations(division)
    assert Calculations.get_last_calculation().get_result() == 4
    assert Calculations.count_history() == 3
