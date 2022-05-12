from quart import Blueprint, websocket

io = Blueprint('socket', __name__, template_folder='templates')


@io.websocket('/ping')
async def ws():
    """Ping the websocket"""
    await websocket.send(f"pong")
