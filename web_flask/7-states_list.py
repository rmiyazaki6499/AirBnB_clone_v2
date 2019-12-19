#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list"""
    storage.reload()
    state_list = []

    for state in storage.all('State').values():
        state_list.append([state.id, state.name])
    return render_template('7-states_list.html', states=state_list)


if __name__ == "__main__":
    app.run()
