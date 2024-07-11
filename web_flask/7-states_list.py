#!/usr/bin/python3
"""This module use flask"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states_lst = storage.all(State)
    for k, v in states_lst.items():
        states_lst[k] = v.to_dict()
    sorted_list = dict(sorted(states_lst.items(),
                              key=lambda item: item[1]['name']))
    return render_template('7-states_list.html', states=sorted_list)


@app.teardown_appcontext
def close_db(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
