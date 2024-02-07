#!/usr/bin/env python3
"""This module function creates a basic flask app"""

from flask import g, Flask, render_template, request
from flask_babel import Babel, get_locale
from flask_babel import gettext as _
import pytz


app = Flask(__name__)
babel = Babel()

users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """This class provides the configuration of languages and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(user_id):
    """Retrieve user information based on the user ID"""
    return users.get(int(user_id))


@app.before_request
def before_request():
    """Set the global user variable 'g.user' before each request"""
    login_as = request.args.get('login_as')
    if login_as:
        g.user = get_user(login_as)
    else:
        g.user = None


def get_locale():
    """This function gets the locale of the client and returns
    content with their preferred language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    accepted_languages = request.accept_languages
    for lang, _ in accepted_languages:
        if lang in app.config['LANGUAGES']:
            return lang

    return app.config['BABEL_DEFAULT_LOCALE']


babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'])
def hello():
    """Render the index.html template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
