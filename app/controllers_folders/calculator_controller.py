from flask import request, render_template, app

from app.controllers_folders.results_controller import ResultsController
from calc.calculator import Calculator
import os.path
import csv


def calculate(value1, value2, operator):
    value1 = float(value1)
    value2 = float(value2)
    if operator == "addition":
        return value1 + value2
    elif operator == 'subtraction':
        return value1 - value2
    elif operator == "multiplication":
        return value1 * value2
    elif operator == 'divide':
        return value1 / value2

    else:
        return "invalid response try again"


class CalculatorController:
    @staticmethod
    def get():
        """Calling Control for Results"""
        return render_template('basicform.html')

    @staticmethod
    def post():
        """Post results"""
        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        # make the tuple
        my_tuple = (value1, value2)
        # if not os.path.isfile("../../datamanager/csv/calculations.csv"):
        # If it doesn't exist then create it
        with open("datamanager/csv/calculations.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([value1, value2, operation, calculate(value1, value2, operation)])

            # 1.0, 1.0, addition, 2.0

        # We will then write here to the csv.

        # this will call the correct operation

        return ResultsController.get()

