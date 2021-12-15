from flask import render_template, app


class IndexController:
    """Calling controls for project"""
    @staticmethod
    def get():
        return render_template('index.html')