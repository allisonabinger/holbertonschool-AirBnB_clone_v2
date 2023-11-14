#!/usr/bin/python3
"""Python script that starts a Flask Web App with various routes """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_state():
    states = storage.all("State")
    """fetching states from storage"""
    return render_template('8-cities_by_state.html', states=states)


@app.teardown_appcontext
def teardown_context(exception=None):
    """closes session for teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
