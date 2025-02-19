#!/usr/bin/python3
"""
Declare a method to handle @app.teardown_appcontext that calls storage.close
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from flask_cors import CORS
from os import getenv


app = Flask(__main__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ Closes the DB """
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """ Returns a JSON formatted 404 status code response """
    return jsonify({'error': 'Not found'}), 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
