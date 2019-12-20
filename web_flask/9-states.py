#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """teardown"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """states"""
    state_list = storage.all(State)
    key = None
    state = None
    if id:
        key = 'State.{}'.format(id)
        if key in state_list.keys():
            state = state_list[key]
    return render_template(
        '9-states.html',
        id=key, state=state,
        state_list=state_list
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
