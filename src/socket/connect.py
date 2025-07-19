from src import socketio


@socketio.on("connect")
def handle_connect():
    print("Client connected to the server")
