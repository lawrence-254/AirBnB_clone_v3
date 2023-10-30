#!/usr/bin/python3
"""Returns a JSON status OK"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Displslays object and their properties"""
    class_dict = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
            }
    obj_result = {class_dict[cls]: storage.count(cls) for cls in class_dict}
    return jsonify(obj_result)
