"""Subtraction Class"""
from operator import sub
from .calculation import Calculation


class Subtraction(Calculation):
    """subtraction calculation object"""

    def subtract(self):
        """get results for test"""
        if isinstance(self.values, list):
            total = self.values[0]
            for num in self.values[1:]:
                total -= num
            self.results = total
            return total
        return self.calculate_dataframe("-", "Subtract", sub)
