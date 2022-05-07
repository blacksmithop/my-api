from flask import Blueprint, jsonify
from time import localtime, strftime

misc = Blueprint('misc', __name__, template_folder='templates')


@misc.route('/time', methods=['GET'])
def currentTime():
    """Return the current time"""
    return jsonify({'time': strftime('%H:%M:%S', localtime()),
                    'message': 'Current time'}), 200
