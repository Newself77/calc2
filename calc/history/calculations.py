"""Calculation history class"""


class Calculations:
    """ get a specific calculation from history"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clear history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """ get a specific calculation from history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """ get a specific calculation from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """ get a specific calculation from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculations(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
