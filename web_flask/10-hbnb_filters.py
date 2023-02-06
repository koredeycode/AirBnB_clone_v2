#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', methods=['GET'], strict_slashes=False)
def hbnb_filters():
    """The hbnb filters view"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return (render_template("10-hbnb_filters.html",
                            states=states,
                            amenities=amenities))


@app.teardown_appcontext
def close_database(exception=None):
    """close the database connection"""
    if exception is None:
        storage.close()
    else:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
