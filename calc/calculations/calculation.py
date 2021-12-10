"""Module containing Calculation Base Class"""
from os.path import isfile
import pandas as pd
import numpy as np
from .logger import get_logger


results_logger, error_logger = get_logger()


class Calculation:
    """calculation abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple, filename=''):
        """constructor method"""
        if isinstance(values, tuple):
            self.values = self.convert_args_to_list_float(values)
        elif isinstance(values, str):
            if isfile(values):
                self.values = pd.read_csv(values)
                self.filename = values
            else:
                raise ValueError(f"{values!r} is an invalid filename!")
        if not hasattr(self, 'filename') and filename != '':
            self.filename = filename
        self.results = None

    @staticmethod
    def convert_args_to_list_float(values):
        """standardize values to list of floats"""
        return list(map(float, values))

    def get_result(self):
        """Returns calculated results"""
        return self.results

    def calculate_dataframe(self, operand, name, func):
        """Calculate values from dataframe"""
        calculated_results = []
        for record_number, (value_1, value_2, result) in self.values.iterrows():
            try:
                calculated_value = func(value_1, value_2)
                if np.isnan(calculated_value):
                    raise TypeError("Invalid Arithmetic Operation")
                print('RECORD_NUMBER:', record_number)
                print(f"{value_1} {operand} {value_2} = {calculated_value}")
                print(f"RESULT: {result}\n")
                calculated_results.append(calculated_value)
                msg = "%s %d %s %d"
                results_logger.info(msg, self.filename, record_number, name, calculated_value)
            except (TypeError, ZeroDivisionError) as error:
                error_logger.error("%s %d %s", repr(error), record_number, self.filename)
        self.results = calculated_results
        return calculated_results
