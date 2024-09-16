from http import HTTPStatus

from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.infrastructure.orm.order_repository import OrderRepository
from app.infrastructure.orm.product_repository import ProductRepository
from app.infrastructure.orm.customer_repository import CustomerRepository

from app.domain.exceptions import EntityNotFoundException
from app.domain.parameters import OrderFilters

from app.application.usecases.order.register_order_usecase import RegisterOrderUseCase
from app.application.usecases.order.find_all_order_usecase import FindAllOrderUseCase
from app.application.presenters.dtos.order_dto import OutputOrderDTO

api = Blueprint("order_api", __name__)


@api.route("/orders", methods=["POST"], endpoint="register_order")
@swag_from({
    'tags': ['Orders'],
    'summary': 'Register a new order',
    'description': 'Endpoint to register a new order in the system.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'customer_id': {'type': 'integer', 'example': 1},
                    'items': {'type': 'array', 'items': {'type': 'integer'}, 'example': [
                        {
                            "product_id": 1,
                            "quantity": 2,
                            "price": 10.00
                        }
                    ]},
                    'total': {'type': 'number', 'format': 'float', 'example': 29.97}
                },
                'required': ['customer_id', 'items', 'total']
            }
        }
    ],
    'responses': {
        HTTPStatus.CREATED: {
            'description': 'Order successfully created',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'customer_id': {'type': 'integer', 'example': 1},
                    'status': {'type': 'string', 'example': 'PENDING'},
                    'items': {'type': 'array', 'items': {'type': 'integer'}, 'example': [
                        {
                            "product_id": 1,
                            "quantity": 2,
                            "price": 10.00
                        }
                    ]},
                    'total': {'type': 'number', 'format': 'float', 'example': 20.00},
                    'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'Product not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Product not found'}
                }
            }
        }
    }
})
def register_order():
    try:
        use_case = RegisterOrderUseCase(
            order_data_provider=OrderRepository(),
            product_data_provider=ProductRepository(),
            customer_data_provider=CustomerRepository()
        )
        order = use_case.execute(**request.json)
        output = OutputOrderDTO.from_domain(order=order).to_dict()
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/orders", methods=["GET"], endpoint="list_order")
@swag_from({
    'tags': ['Orders'],
    'summary': 'List all orders',
    'description': 'Endpoint to retrieve a list of all orders in the system.',
    'parameters': [
        {
            'name': 'customer_id',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'ID Customer',
            'example': 1
        }
    ],
    'responses': {
        HTTPStatus.OK: {
            'description': 'A list of orders',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'customer_id': {'type': 'integer', 'example': 1},
                        'status': {'type': 'string', 'example': 'RECEIVED'},
                        'items': {'type': 'array', 'items': {'type': 'integer'}, 'example': [
                            {
                                "product_id": 1,
                                "quantity": 2,
                                "price": 10.00
                            }
                        ]},
                        'total': {'type': 'number', 'format': 'float', 'example': 20.00},
                        'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                    }
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'Orders not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Orders not found'}
                }
            }
        }
    }
})
def list_order():
    try:
        use_case = FindAllOrderUseCase(order_data_provider=OrderRepository())
        orders = use_case.execute(OrderFilters(
            customer_id=request.args.get("customer_id"),
            order=request.args.get("order"),
            sort=request.args.get("sort"),
            status=request.args.get("status").split(",") if request.args.get("status") else None
        ))
        output = [OutputOrderDTO.from_domain(order=order).to_dict() for order in orders]
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
