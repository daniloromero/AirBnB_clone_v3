#!/usr/bin/python3
"""script that starts Flask web applicationlistening on 0.0.0.0 port 5000"""
from models import storage
from api.v1.views import app_views
from models.state import State
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def close_db(error):
     """ Remove the current SQLAlchemy Session """
     storage.close()

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404  

if __name__ == "__main__":
    """ Main Function"""
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
