#!/usr/bin/python3
"""Python script that starts a Flask Web App that says 'Hello HBNB!'"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hi_holbies():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
