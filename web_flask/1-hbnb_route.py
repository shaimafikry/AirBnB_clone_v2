#!/usr/bin/python3
"""my first module"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello world from the root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """hbnb"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # debug=True, which will be beneficial if you plan to make changes
    # and want the server to automatically reload
    # and provide helpful debugging information.
