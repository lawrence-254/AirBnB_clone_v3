#!/usr/bin/python3
"""view for State objects that handles all default RESTFul API action"""


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """
    Fetches all state objects

    Returns:
        A dictionary of state object
    """
    states = []
    for state in storage.all("State").values():
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
        strict_slashes=False)
def get_state_by_id(state_id=None):
    """
    Fetches all state objects by id

    Args:
        state_id (str): The UUID4 string representing a State object.

    Returns:
        A state object in JSON format or 404 if not found
    """
    if state_id:
        for state in storage.all("State").values():
            if state.id == state_id:
                return jsonify(state.to_dict())
        abort(404)
