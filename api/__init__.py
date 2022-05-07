from ensurepip import version
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():
    return jsonify(
        {
            'version': '1.0.0',
            'message': 'Hello, World!'
        }), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', path=request.path), 404


@app.route("/site-map")
def site_map():
    print(app.url_map)
    endpoints = [rule.endpoint for rule in app.url_map.iter_rules()]
    return jsonify(endpoints), 200
