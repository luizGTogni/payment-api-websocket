import os
import uuid
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        bank_payment_id = str(uuid.uuid4())

        hash_payment = f"{os.urandom(12).hex()}_{bank_payment_id}"

        img = qrcode.make(hash_payment)
        file_name = f"qr_code_payment_{bank_payment_id}"
        img.save(f"{os.getcwd()}/static/img/{file_name}.png")

        return {"bank_payment_id": bank_payment_id, "qr_code_path": file_name}

    def remove_qr_code(self, bank_payment_id):
        if os.path.exists(
            f"{os.getcwd()}/static/img/qr_code_payment_{bank_payment_id}.png"
        ):
            os.remove(f"{os.getcwd()}/static/img/qr_code_payment_{bank_payment_id}.png")
