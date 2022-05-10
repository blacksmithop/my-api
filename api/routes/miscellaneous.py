from quart import Blueprint, jsonify, render_template
from time import localtime, strftime
from aiohttp import ClientSession

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


@misc.route('/github', methods=['GET'])
async def githubStats():
    """Return github stats for an user"""
    async with ClientSession() as session:
        async with session.get('https://api.github.com/users/blacksmithop') as response:
            data = await response.json()
            print(data['login'])
            return await render_template('github.html', data=data)
