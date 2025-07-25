from src import app
from src.models.payment import Payment
from flask import render_template


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    payment_current = Payment.query.get(payment_id)

    if not payment_current:
        return render_template("404.html")

    value_brl = (
        "{:,.2f}".format(payment_current.value)
        .replace(",", "v")
        .replace(".", ",")
        .replace("v", ".")
    )

    if payment_current.paid:
        return render_template(
            "confirmed_payment.html", value=value_brl, payment_id=payment_current.id
        )

    host = "http://localhost:5000"
    return render_template(
        "payment.html",
        host=host,
        payment_id=payment_current.id,
        file_name=payment_current.qr_code,
        value=value_brl,
    )
