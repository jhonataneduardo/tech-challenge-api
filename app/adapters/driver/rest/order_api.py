from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.adapters.driven.orm.order_repository import OrderRepository
from app.adapters.driven.orm.product_repository import ProductRepository
from app.adapters.driven.orm.customer_repository import CustomerRepository

from app.domain.services.order_service import OrderService
from app.domain.exceptions import EntityNotFoundException

from app.adapters.driver.dtos.order_dto import OutputOrderDTO

service = OrderService(
    order_repository=OrderRepository(),
    product_repository=ProductRepository(),
    customer_repository=CustomerRepository()
)

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
        order = service.create_order(**request.json)
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
        orders = service.all_orders(**request.args)
        output = [OutputOrderDTO.from_domain(order=order).to_dict() for order in orders]
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
