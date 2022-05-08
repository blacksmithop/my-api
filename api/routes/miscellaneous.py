from flask import Blueprint, jsonify, render_template
from time import localtime, strftime

misc = Blueprint('misc', __name__, template_folder='templates')


@misc.route('/time', methods=['GET'])
def currentTime():
    """Return the current time"""
    return jsonify({'time': strftime('%H:%M:%S', localtime()),
                    'message': 'Current time'}), 200


@misc.route('/testapi', methods=['GET'])
def testAPI():
    """Test an API endpoint"""
    return render_template('testapi.html')
