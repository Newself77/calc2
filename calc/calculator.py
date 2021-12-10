""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.history.calculations import Calculations
from calc.calculations.division import Division


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculations(calculation)
        return calculation.add()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        Calculations.add_calculations(calculation)
        return calculation.subtract()

    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        Calculations.add_calculations(calculation)
        return calculation.multiply()

    @staticmethod
    def divide_numbers(*args):
        """divide numbers"""
        calculation = Division(args)
        Calculations.add_calculations(calculation)
        return calculation.divide()

    @classmethod
    def clear_history(cls):
        """will clear history"""
        Calculations.clear_history()
