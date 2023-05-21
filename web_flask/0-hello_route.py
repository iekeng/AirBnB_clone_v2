#!/usr/bin/python3
""" Set strict_slashes to false in route definition.
    Any route with or without a trailing slash will
    trigger the specific decorated function.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ This function displays 'Hello HBNB'
        when the '/' route is visited on the
        server
    """

    return 'Hello HBNB!'

if __name__ == '__main__'():
    app.run(host='0.0.0.0', port=5000)
