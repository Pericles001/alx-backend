#!/usr/bin/env python3
""" 3. Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel
s
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get_locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """ hello.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
