import csv

from flask import render_template, flash


class ResultsController:

    @staticmethod
    def get():
        """Calling for result of calculator"""
        with open("datamanager/csv/calculations.csv", newline='') as file:
            reader = csv.reader(file)
            for i in reader:
                flash(i)
        return render_template("result.html")

