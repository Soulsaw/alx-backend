#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request
"""Import module doc"""
app = Flask(__name__)


def get_locale() -> str:
    """Define the babel local time"""
    return request.accept_languages.best_match(["en", "fr"])


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def home() -> str:
    """The root url for the home page"""

    return render_template('3-index.html')


if __name__ == "__main__":
    """The main fun"""
    app.run()
