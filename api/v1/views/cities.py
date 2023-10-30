#!/usr/bin/python3
'''City model methods'''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City


@app_views.route('/states/<string:state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """Retrieves the list of all city objects."""
    state_obj = storage.get("State", state_id)
    if state_obj is None:
        abort(404)
    cities = [city.to_dict() for city in state_obj.cities]
    return jsonify(cities)


@app_views.route('/cities/<string:city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """ Retrieves a City object based on `city_id`"""
    city_obj = storage.get("City", city_id)
    if city_obj is None:
        abort(404)
    return jsonify(city_obj.to_dict())
