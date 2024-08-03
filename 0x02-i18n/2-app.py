#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel
"""Import module doc"""
app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Define the babel local time"""
    return request.accept_languages.best_match(["en", "fr"])


@app.route("/", strict_slashes=False)
def home():
    """The root url for the home page"""
    return render_template('2-index.html')


if __name__ == "__main__":
    """Definition of the main program"""
    app.run()
