#!/usr/bin/python3
"""Python script that starts a Flask Web App with various routes """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hi_holbies():
    """says Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    """says HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """
    displays the letter C then text entered in url
    also replaces underscores with a space.
    """
    c_text = text.replace('_', ' ')
    return 'C {}'.format(c_text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_py_text(text):
    """
    displays Python and 'is cool' if no text given, or <text> afterwards
    also replaces underscores with a space
    """
    py_text = text.replace('_', ' ')
    return 'Python {}'.format(py_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


"""
@app.route('/number/<n>', strict_slashes=False)
def is_it_a_num(n):
    if type(n) is int:
        return '{} is a number'.format(n)
"""
