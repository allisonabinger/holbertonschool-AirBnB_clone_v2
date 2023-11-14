@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays lists of states and cities from db storage"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)
