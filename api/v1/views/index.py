#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """App status"""
    return {"status": "OK"}
