from .routes.miscellaneous import misc
from .routes.utility import util
from quart import Quart, jsonify
from .utils.middleware import SimpleMiddleware

app = Quart(__name__, static_folder='static')

app.asgi_app = SimpleMiddleware(app.asgi_app)

# import & register blueprints

app.register_blueprint(misc)
app.register_blueprint(util)


@app.route('/', methods=['GET'])
async def index():
    """The index page"""
    return jsonify(
        {
            'version': '1.0.0',
            'message': 'Hello, World!'
        }), 200


@app.route("/site-map", methods=['GET'])
async def listEndpoints():
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
