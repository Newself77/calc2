"""This is our calculation base class / Abstract Class"""


class Calculation:
    """ This is the testing class"""
    # constructor and it is the first function called when an object of the class is instantiated
    def __init__(self, value_a, value_b):
        # self references the instances object of the class
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        """ This is the testing class"""
        return cls(value_a, value_b)
