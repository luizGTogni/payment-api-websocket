from flask import jsonify, request
from src import app, db, socketio
from src.models.payment import Payment
from src.payments.pix import Pix


@app.route("/payments/pix/confirmation", methods=["PATCH"])
def pix_confirmation():
    body = request.get_json()

    if "bank_payment_id" not in body or "value" not in body:
        return jsonify({"error": "Invalid payment data"}), 400

    payment = Payment.query.filter_by(bank_payment_id=body["bank_payment_id"]).first()

    if not payment or payment.paid:
        return jsonify({"error": "Payment not found"}), 404

    if body["value"] != payment.value:
        return jsonify({"error": "Invalid payment data"}), 400

    payment.paid = True
    db.session.commit()
    socketio.emit(f"payment-confirmed-{payment.id}")
    pix_obj = Pix()
    pix_obj.remove_qr_code(payment.bank_payment_id)

    return jsonify({"message": "The payment has been confirmed"}), 200
