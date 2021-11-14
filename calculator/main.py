""" This is the increment function"""
# first import the addition namespace
from calc.addition import Addition


class Calculator:
    """ This is the Calculator class"""
    history = []

    def __init__(self):
        self.result = None

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        # -1 get the last item to the list automatically and you can expect it to have the get results method
        return Calculator.history[-1].getResults()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        # create an addition object using a factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        # addition = Addition(value_a,value_b) <-this is not good but will work. It will be repeated to much
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return value_a - value_b

    @staticmethod
    def multiply_numbers(vale_a, value_b):
        """ multiplication of two numbers and store the result"""
        return vale_a * value_b

    def get_result(self):
        pass
