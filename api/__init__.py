from quart import Quart, jsonify

from .routes.miscellaneous import misc
from .routes.utility import util
from .routes.websocket import io

from .utils.middleware import SimpleMiddleware
from .utils.cache import cache

app = Quart(__name__, static_folder='static')
cache.init_app(app)

app.asgi_app = SimpleMiddleware(app.asgi_app)

# import & register blueprints
blueprints = [misc, util, io]
for blueprint in blueprints:
    try:
        app.register_blueprint(blueprint)
    except Exception as e:
        print(f'[ERROR] Failed to load Blueprint\n {e}')


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
