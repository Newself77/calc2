"""This addition calculation that inherits the value A and value B from the calculation class"""
# this a namespace it is like files & folders the classes are files. Folders organize the classes
# a folder & file path is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation


# This is how you extend the Addition class with the Calculation
class Multiplication(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        """this multiplies a and b"""
        # use self to reference data contained in instance of the object. This is encapsulation
        return self.value_a * self.value_b
