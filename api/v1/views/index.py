#!/usr/bin/python3
"""Returns a JSON status OK"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})
