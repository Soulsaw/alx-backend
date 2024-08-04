#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
"""Import module doc"""
app = Flask(__name__)
LANGUAGES = ['en', 'fr']
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> str:
    """Define the babel local time"""
    user = getattr(g, 'user', None)
    if user is not None:
        locale = user.get('locale')
        if locale in LANGUAGES:
            return locale
    return request.accept_languages.best_match(["en", "fr"])


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


def get_user(id) -> dict:
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
    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    """Starting flask app"""
    app.run()
