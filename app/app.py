"""A simple flask web app"""
from flask import Flask, request, render_template

from app.controllers_folders.index_cntroller import IndexController
from app.controllers_folders.calculator_controller import CalculatorController
from app.controllers_folders.results_controller import ResultsController
from calc.calculator import Calculator


app = Flask(__name__)
app.secret_key = "wiuhWDQFWw2oiue*^&$(*@hfo29843fh2"


@app.route("/")
def index():
    """index  Route Response"""
    return IndexController.get()


@app.route("/calculator", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        return CalculatorController.post()
    else:
        return CalculatorController.get()


@app.route("/bad/<value1>/<value2>")
def bad_calc(value1, value2):
    """bad calc Route Response"""
    result = value1 + value2
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response


@app.route("/good/<float:value1>/<float:value2>")
def good_calc(value1, value2):
    """good calc Route Response"""
    my_tuple = (value1, value2)
    Calculator.addition(my_tuple)
    response = "The result of the calculation is: " + str(Calculator.get_last_result_value()) + '<a href="/"> back</a>'
    return response


@app.route("/result")
def results():
    return ResultsController.get()
