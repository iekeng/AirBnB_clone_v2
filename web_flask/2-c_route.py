#!/usr/bin/python3
""" Set strict_slashes to false in route definition.
    Any route with or without a trailing slash will 
    trigger the specific decorated function.
"""

# from flask import Flask
# app = Flask(__name__)

@app.route('/', strict_slashes=False)
def 1-hbnb_route():
    """ This function displays 'Hello HBNB'
        when the '/' route is visited on the 
        server.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def 1-hbnb_route():
    """ This function displays `HBNB`
        when the '/hbnb' route is visited on the 
        server.
    """
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def 1-hbnb_route(text='cool'):
    """ This function displays `C <text>`
        when the '/c/' route is visited on the 
        server.
    """
    text = text.replace('_', ' ')
    result = "C %s" % escape(text)
    return result
