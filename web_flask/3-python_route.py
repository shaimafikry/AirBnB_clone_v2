#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the
text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def bnb():
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<data>', strict_slashes=False)
def hello_python(data="is cool"):
    return f"Python {data.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
