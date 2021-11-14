"""This is the addition calculation that inherits the value A and value B from the calculation class"""
# this a namespace it is like files & folders the classes are files. Folders organize the classes
# Looks like a folder & file path but it is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation


# This is how you extend the Addition class with the Calculation
class Multiplication(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def getResult(self):
        # you need to use self to reference the data contained in the instance of the object. This is encapsulation
        return self.value_a * self.value_b
