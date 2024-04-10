#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask_babel import Babel
from flask import Flask, render_template
app = Flask(__name__)
"""Import module doc"""


class Config:
    LANGUES = ["en", "fr"]


babel = Babel(app)

app.config.from_object(Config)
babel.default_locale = "en"
babel.default_timezone = "UTC"


@app.route("/", strict_slashes=False)
def home():
    """The root url for the home page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    """Definition of the main program"""
    app.run()
