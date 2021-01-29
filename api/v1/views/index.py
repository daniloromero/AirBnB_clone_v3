#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """App status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ endpoint that retrieves the number of each objects by type"""
    classes = {"amenities": Amenity, "cities": City, "places": Place,
               "reviews": Review, "states": State, "users": User}
    count_of_objs = {}
    for key, value in classes.items():
        count_of_objs[key] = storage.count(value)
        print(count_of_objs)
    return jsonify(count_of_objs)
