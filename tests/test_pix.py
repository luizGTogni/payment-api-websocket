import sys

sys.path.append("../")

import pytest
import os
from src.payments.pix import Pix

bank_payment_id_global = []


@pytest.fixture(scope="session")
def pix_instance_session():
    pix_instance = Pix()
    return pix_instance


def test_pix_create_payment(pix_instance_session):
    payment_info = pix_instance_session.create_payment(base_dir="../")

    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info

    assert os.path.isfile(f"../static/img/{payment_info["qr_code_path"]}.png")
    bank_payment_id_global.append(payment_info["bank_payment_id"])


def test_pix_remove_qr_code(pix_instance_session):
    qr_code_removed = pix_instance_session.remove_qr_code(
        bank_payment_id=bank_payment_id_global[0], base_dir="../"
    )

    file_path = f"../static/img/qr_code_payment_{bank_payment_id_global[0]}.png"
    assert qr_code_removed == True
    assert os.path.isfile(file_path) == False
