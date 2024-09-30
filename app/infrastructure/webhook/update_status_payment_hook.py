from http import HTTPStatus
from flask import Blueprint, request, jsonify

from app.infrastructure.orm.payment_repository import PaymentRepository
from app.infrastructure.orm.order_repository import OrderRepository

from app.domain.exceptions import EntityNotFoundException

from app.application.usecases.payment.update_status_payment_usecase import UpdateStatusPaymentUseCase

hook = Blueprint("payment_hook", __name__)


@hook.route("/hooks/update-status-payment", methods=["POST"], endpoint="hook_update_status_payment")
def hook_update_status_payment():
    try:
        use_case = UpdateStatusPaymentUseCase(
            payment_data_provider=PaymentRepository(),
            order_data_provider=OrderRepository()
        )
        # product = use_case.execute()
        return jsonify({"test": "Ok"}), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
