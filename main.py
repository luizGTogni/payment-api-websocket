from src import socketio, app


if __name__ == "__main__":
    socketio.run(app=app, debug=True)
