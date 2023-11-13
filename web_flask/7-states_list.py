"""Python script that starts a Flask Web App with various routes """
from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays lists of states and cities from db storage"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(error=None):
    """ends SQLAlchemy session"""
   """ stg = getattr(g, "storage", None)
    if stg is not None:
        stg.close()"""
""""""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)