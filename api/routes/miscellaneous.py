import quart.flask_patch
from quart import Blueprint, jsonify, render_template
from time import localtime, strftime
from aiohttp import ClientSession
from ..utils.cache import cache

misc = Blueprint('Misc', __name__, template_folder='templates')


@misc.route('/time', methods=['GET'])
async def currentTime():
    """Return the current time"""
    return jsonify({'time': strftime('%H:%M:%S', localtime()),
                    'message': 'Current time'}), 200


@misc.route('/testapi', methods=['GET'])
async def testAPI():
    """Test an API endpoint"""
    return await render_template('testapi.html')


async def getUser(username: str):
    async with ClientSession() as session:
        async with session.get(f'https://api.github.com/users/{username}') as response:
            return await response.json()


@cache.cached(timeout=None)
@misc.route('/github/', defaults={'username': 'blacksmithop'})
@misc.route('/github/<username>', methods=['GET'])
async def githubStats(username=None):
    """Return github stats for an user"""
    data = await getUser(username)
    return await render_template('github.html', data=data)
