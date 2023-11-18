#!/usr/bin/python3
"""Python script that starts a Flask Web App with various routes """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hi_holbies():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    c_text = text.replace('_', ' ')
    return 'C {}'.format(c_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
