#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', methods=['GET'], strict_slashes=False)
def states():
    """The state list view"""
    states = storage.all(State)
    return (render_template("9-states.html", context=states))


@app.route('/states/<id>', methods=['GET'], strict_slashes=False)
def states_id(id):
    """The state list view"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return (render_template("9-states.html", context=state))
    return (render_template("9-states.html"))


@app.teardown_appcontext
def close_database(exception=None):
    """close the database connection"""
    if exception is None:
        storage.close()
    else:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
