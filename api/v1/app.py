#!/usr/bin/python3
"""
Declare a method to handle @app.teardown_appcontext that calls storage.close
"""
from api.v1.views import app_views
from flask import Flask
from models import storage


app = Flask(__main__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
