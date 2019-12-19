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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list"""
    storage.reload()

    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states"""
    storage.reload()

    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run()
