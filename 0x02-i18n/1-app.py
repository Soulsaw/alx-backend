#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask_babel import Babel
from flask import Flask, render_template
"""Import module doc"""
app = Flask(__name__)


class Config:
    """Doc of the config class"""
    LANGUES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app, locale_selector=Config)


@app.route("/", strict_slashes=False)
def home():
    """The root url for the home page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    """Definition of the main program"""
    app.run()
