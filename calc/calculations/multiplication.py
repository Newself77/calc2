"""Multiplication Class"""
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """multiplication calculation object"""

    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result

    @classmethod
    def create(cls, tuple_values):
        pass


def multiplication():
    return None