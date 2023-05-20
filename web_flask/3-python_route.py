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
        server. 
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb:
    """ This function displays `HBNB`
        when the '/hbnb' route is visited on the 
        server. <text> default is set to 'cool'.
    """
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text='cool'):
    """ This function displays `C <text>`
        when the '/c/' route is visited on the 
        server. <text> default is set to 'cool'.
    """
    text = text.replace('_', ' ')
    result = "C %s" % escape(text)
    return result

@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text='is cool'):
    """ This function displays `Python <text>`
        when the '/python/' route is visited on the 
        server. 
    """
    text = text.replace('_', ' ')
    result = "Python %s" % escape(text)
    return result