#!/usr/bin/env python3
"""This module function creates a basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale
from flask_babel import gettext as _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """This class provides the configuration of languages and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """This function gets the locale of the client and returns
    content with their preferred language"""
    accepted_languages = request.accept_languages

    for lang, _ in accepted_languages:
        if lang in app.config['LANGUAGES']:
            return lang

    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/', methods=['GET'])
def hello():
    """Render the index.html template.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
