#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request
from typing import List
"""Import module doc"""
app = Flask(__name__)
LANGUAGES = ['en', 'fr']


def get_locale() -> List:
    """Define the babel local time"""
    locale = request.args.get('locale')
    if locale in LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(["en", "fr"])


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def home():
    """The root url for the home page"""

    return render_template('4-index.html')
