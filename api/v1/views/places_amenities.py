#!/usr/bin/python3
'''places amenity module'''
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, storage_t
from models.amenity import Amenity
