"""Multiplication Class"""
from operator import mul
from .calculation import Calculation


class Multiplication(Calculation):
    """multiplication calculation object"""

    def multiply(self):
        """get results for test"""
        if isinstance(self.values, list):
            total = 1
            for num in self.values:
                total *= num
            self.results = total
            return total
        return self.calculate_dataframe("*", "Multiplication", mul)
