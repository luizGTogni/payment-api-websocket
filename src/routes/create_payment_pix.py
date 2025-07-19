from datetime import datetime, timedelta, timezone
from flask import request, jsonify
from src import app, db
from src.models.payment import Payment
from src.payments.pix import Pix


@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    body = request.get_json()

    if "value" not in body:
        return jsonify({"error": "Invalid value"}), 409

    expiration_date = datetime.now(timezone.utc) + timedelta(minutes=15)
    new_payment = Payment(value=body["value"], expiration_date=expiration_date)

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment()

    new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]
    new_payment.qr_code = data_payment_pix["qr_code_path"]

    db.session.add(new_payment)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "The payment has been created",
                "payment": new_payment.to_dict(),
            }
        ),
        201,
    )
