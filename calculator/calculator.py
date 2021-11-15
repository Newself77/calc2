""" This is the increment function"""
# first import the addition namespace
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """ This is the Calculator class"""
        # will connect history with class
        return Calculator.history[0].getResult()

    @staticmethod
    def clear_history():
        """ This is the Calculator class"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """ This is the Calculator class"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """ This is the Calculator class"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """ This is the Calculator class"""
        # -1 the list automatically and you can expect it to have the get results method
        return Calculator.history[-1].getResult()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        # create an addition object using a factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        # addition = Addition(value_a,value_b) <-will work. It will be repeated to much
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    # this is on example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        # create an subtraction object using a factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
        # addition = Addition(value_a,value_b) <-will work. It will be repeated to much
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(vale_a, value_b):
        """ multiplication of two numbers and store the result"""
        # shorthand to create the multiplication object and added it the history in one line
        Calculator.add_calculation_to_history(Multiplication.create(vale_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()

    def get_result(self):
        """ This is the Calculator class"""
