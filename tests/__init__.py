"""Calculation history Class"""


class Calculations:
    """Testing Calculation"""
    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """Clear history in test results"""
        Calculations.history.clear()
        return True

    @staticmethod
    def get_last_calculation():
        """ Test for last call"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """Test for first calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
