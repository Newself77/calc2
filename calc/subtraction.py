"""This is subtraction cal inherits value A and value B from calculation class"""
# namespace is files and folders the classes are files and the folders organize the classes
# Its a folder, file path but it is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation


# This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    """The sub class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def getResult(self):
        """Subtraction of value a and b"""
        # use self to reference data contained in instance of the object. encapsulation
        return self.value_a - self.value_b
