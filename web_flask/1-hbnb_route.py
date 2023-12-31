#!/usr/bin/python3
"""Python script that starts a Flask Web App with different text displayed
based on route provided in url"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hi_holbies():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
