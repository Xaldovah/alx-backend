#!/usr/bin/env python3
"""This module function creates a basic flask app"""

import os
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """This class provides the configuration of languages and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """This function gets the locale of the client and returns
    content with their preferred language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def hello():
    """Render the index.html template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
