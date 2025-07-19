import os
from flask import send_file
from src import app


@app.route("/payments/pix/qr_code/<file_name>", methods=["GET"])
def get_qrcode_pix(file_name):
    return send_file(f"{os.getcwd()}/static/img/{file_name}.png", mimetype="image/png")
