#!/usr/bin/python3
""" strict_slashes set to false in all route definitions.
    Any route with or without a trailing slash will trigger 
    the specific decorated function.
"""


# from flask import Flask
# app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ This function displays 'Hello HBNB'
        when the '/' route is visited on the 
        server. <text> default is set to 'cool'
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This function displays `HBNB`
        when the '/hbnb' route is visited on the 
        server. <text> default is set to 'cool'.
    """
    return 'HBNB!'