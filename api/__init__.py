from .routes.miscellaneous import misc
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

# import & register blueprints

app.register_blueprint(misc)


@app.route('/', methods=['GET'])
def index():
    """The index page"""
    return jsonify(
        {
            'version': '1.0.0',
            'message': 'Hello, World!'
        }), 200


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page"""
    return render_template('404.html', path=request.path), 404


@app.route("/site-map", methods=['GET'])
def listEndpoints():
    """Returns a site map of all available endpoints"""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = {
                'description': app.view_functions[rule.endpoint].__doc__,
                'methods': list(rule.methods),
                'endpoint': rule.endpoint,
            }
    return jsonify({
        'message': 'List of available endpoints',
        'endpoints': func_list
    }), 200
