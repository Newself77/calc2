"""Division Calculation Module"""
from operator import truediv
from .calculation import Calculation


class Division(Calculation):
    """Division Calculation Class"""
    def divide(self):
        """Calculates Divison results"""
        if isinstance(self.values, list):
            try:
                self.results = self.values[0] / self.values[1]
                return self.results
            except (TypeError, ZeroDivisionError):
                return float("inf")
        return self.calculate_dataframe("/", "Division", truediv)
