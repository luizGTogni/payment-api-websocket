from src import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, default=0)
    paid = db.Column(db.Boolean, nullable=False, default=False)
    bank_payment_id = db.Column(db.String(200))
    qr_code = db.Column(db.String(100))
    expiration_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "expiration_date": self.expiration_date,
        }
