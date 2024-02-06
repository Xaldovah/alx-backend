#!/usr/bin/env python3
"""This module function creates a basic flask app"""

import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    """Render the index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
