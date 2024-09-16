from http import HTTPStatus
from flask import Blueprint, request, jsonify

from app.infrastructure.orm.payment_repository import PaymentRepository
from app.infrastructure.orm.payment_type_repository import PaymentTypeRepository
from app.infrastructure.orm.order_repository import OrderRepository

from app.domain.exceptions import EntityNotFoundException

from app.application.usecases.payment.register_payment_usecase import RegisterPaymentUseCase
from app.application.usecases.payment.list_all_payments_usecase import ListAllPaymentsUseCase
from app.application.presenters.dtos.payment_dto import OutputPaymentDTO

api = Blueprint("payment_api", __name__)


@api.route("/payments", methods=["POST"], endpoint="register_payment")
def register_payment():
    try:
        use_case = RegisterPaymentUseCase(
            payment_data_provider=PaymentRepository(),
            payment_type_data_provider=PaymentTypeRepository(),
            order_data_provider=OrderRepository()
        )
        payment = use_case.execute(**request.json)
        output = OutputPaymentDTO.from_domain(payment=payment).to_dict()
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND


@api.route("/payments", methods=["GET"], endpoint="list_payment")
def list_payment():
    try:
        use_case = ListAllPaymentsUseCase(payment_data_provider=PaymentRepository())
        payments = use_case.execute(**request.args)
        return jsonify([OutputPaymentDTO.from_domain(payment=payment).to_dict() for payment in payments]), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": err.args}), HTTPStatus.INTERNAL_SERVER_ERROR
