from os import getenv

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

load_dotenv()

app = Flask(__name__, static_folder="../static")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY")

db = SQLAlchemy(app)
socketio = SocketIO(app)

from src.routes import (
    create_payment_pix,
    get_qrcode_pix,
    payment_pix_page,
    pix_confirmation,
)
from src.socket import connect
