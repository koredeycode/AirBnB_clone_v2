#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/cities_by_states', methods=['GET'], strict_slashes=False)
def cities_by_states():
    """The state list view"""
    states = storage.all(State)
    return (render_template("8-cities_by_states.html", states=states))


@app.teardown_appcontext
def close_database(exception=None):
    if exception is None:
        storage.close()
    else:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
