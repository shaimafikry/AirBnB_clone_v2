#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template

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


@app.route('/python/', defaults={"data": "is cool"}, strict_slashes=False)
@app.route('/python/<data>', strict_slashes=False)
def hello_python(data="is_cool"):
    return f"Python {data.replace('_', ' ')}"


# int:n takes only integers directly
@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    n = int(n)
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def page_number(n):
    n = int(n)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
