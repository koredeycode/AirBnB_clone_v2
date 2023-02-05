#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """The index view"""
    return ("Hello HBNB!")


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """The hbnb view"""
    return ("HBNB")


@app.route('/c/<string:text>', methods=['GET'], strict_slashes=False)
def c(text):
    """The hbnb view"""
    return ("C {}".format(text).replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)