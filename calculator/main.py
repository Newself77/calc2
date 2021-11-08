""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""

    result = 3
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result
    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result
    def multiply_numbers(self, vale_a, value_b):
        """ tests multiplication of two numbers"""
        self.result = vale_a * value_b
        return self.result
    def divide_numbers(self, value_a, value_b):
        """ tests divsion of two numbers """
        self.result = value_a / value_b
        return self.result
