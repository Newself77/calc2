"""This is the addition calc that inherits the value A & value B from the calculation class"""
# Called a namespace it is like files & folders the classes are files & the folders organize the classes
# It looks like a folder, file path but it is sort of a virtual representation of how the program is organized
from calc.calculation import Calculation


# This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def getResult(self):
        # you need to use self to reference the data contained in the instance of the object. This is encapsulation
        return self.value_a + self.value_b
