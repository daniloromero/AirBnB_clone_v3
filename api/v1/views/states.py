#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import jsonify
from models.state import State
from models import storage
from flask import jsonify, abort, request


@app_views.route('/states', strict_slashes=False)
def all_states():
    """Retrieves the list of all State objects"""
    all_states = storage.all(State).values()
    states_list = []
    for item in all_states:
        states_list.append(item.to_dict())
    return jsonify(states_list)

@app_views.route('/states/<state_id>', strict_slashes=False)
def state_by_id(state_id):
    """Retrieves a State object by id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'],strict_slashes=False)
def delete_state_by_id(state_id):
    """Deletes a State object by id"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)
    else:
        state.delete()
        storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'],strict_slashes=False)
def post_state_by_id():
    """Creates a State object """

    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'],strict_slashes=False)
def put_state_by_id(state_id):
    """Updates a State object """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    state.name = data['name']
    storage.save()
    return jsonify(state.to_dict()), 200
