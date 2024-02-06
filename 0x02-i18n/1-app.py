#!/usr/bin/env python3
"""This module function creates a basic flask app"""

import os
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """This class provides the configuration of languages and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'])
def hello():
    """Render the index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
