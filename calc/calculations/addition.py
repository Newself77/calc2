"""Addition Calculation Module"""
from operator import add
from .calculation import Calculation


class Addition(Calculation):
    """Addition Calculation Class"""
    def add(self):
        """List rows and columns"""
        if isinstance(self.values, list):
            total = 0
            for num in self.values:
                total += num
            self.results = total
            return total
        return self.calculate_dataframe("+", "Addition", add)
