from quart import Blueprint, render_template, request, websocket

util = Blueprint('Util', __name__, template_folder='templates')


@util.errorhandler(404)
async def page_not_found(e):
    """Custom 404 page"""
    return await render_template('404.html', path=request.path), 404



