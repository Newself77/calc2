from flask import render_template


class IndexController:
    """Calling controls for project"""
    @staticmethod
    def get():
        return render_template("index.html")


