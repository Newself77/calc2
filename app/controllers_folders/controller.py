from flask import render_template

name_of_website = "The Internet with Python"


class Controller:
    @staticmethod
    def base_render(title="Not Found", content=render_template("error.html", error_message="Page not found")):
        return render_template("base.html", content=content, title=f"{title} - {name_of_website}")
