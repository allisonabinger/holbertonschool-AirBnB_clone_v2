#!/usr/bin/python3
"""Python script that starts a Flask Web App with various routes """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """returns the key/value pair for a list of states"""
    states = storage.all(State).values() 
    """fetching states from storage - gettings list of dictionary objects"""
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_context(exception=None):
    """closes session for teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
