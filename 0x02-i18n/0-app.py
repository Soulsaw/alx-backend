#!/usr/bin/env python3
"""
Doc for a basic flask app
"""
from flask import Flask, render_template
"""Import module doc"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """The root url for the home page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """Definition of the main program"""
    app.run()
