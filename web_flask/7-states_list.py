#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', methods=['GET'], strict_slashes=False)
def states_list():
    """The state list view"""
    states = storage.all(State)
    return (render_template("7-states_list.html", states=states))


@app.teardown_appcontext
def close_database(exception=None):
    """close the database connection"""
    if exception is None:
        storage.close()
    else:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)