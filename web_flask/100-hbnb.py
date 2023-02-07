#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """The hbnb view"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return (render_template("100-hbnb.html",
                            states=states,
                            amenities=amenities,
                            places=places))


@app.teardown_appcontext
def close_database(exception=None):
    """close the database connection"""
    if exception is None:
        storage.close()
    else:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
