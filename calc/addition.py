"""This is the addition calc that inherits the value A & value B from the calculation class"""
# Namespace it is like files & folders the classes are files & the folders organize the classes
# Folder, file path but it is a virtual representation of how the program is organized
from calc.calculation import Calculation


# This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        """This shows the added value of a and b"""
        # use self to reference data contained in the instance of the object. encapsulation
        return self.value_a + self.value_b
