#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import List, Dict
"""Import module doc"""
app = Flask(__name__)
LANGUAGES = ['en', 'fr']
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> List:
    """Define the babel local time"""
    locale = request.args.get('locale')
    if locale in LANGUAGES:
        return locale
    user = getattr(g, 'user', None)
    if user and user.get('locale') in LANGUAGES:
        return user.get('locale')
    return request.accept_languages.best_match(['en', 'fr'])


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


def get_user(id) -> Dict:
    """This function return the given user dictionnary"""
    try:
        return users.get(int(id), None)
    except ValueError:
        pass


@app.before_request
def before_request():
    """Define the user before"""
    id = request.args.get('login_as', None)
    if id:
        user = get_user(id)
        g.user = user
        if user is not None:
            g.locale = g.user.get('locale')
    else:
        g.user = None


@app.route("/", strict_slashes=False)
def home():
    """The root url for the home page"""
    return render_template('6-index.html', user=g.user)
