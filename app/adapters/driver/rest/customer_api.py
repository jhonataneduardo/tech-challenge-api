from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.adapters.driven.orm.customer_repository import CustomerRepository

from app.domain.services.customer_service import CustomerService
from app.domain.exceptions import CustomerAlreadyExistsException, CustomerNotFoundException, EntityNotFoundException

from app.adapters.driver.dtos.customer_dto import OutputCustomerDTO

service = CustomerService(repository=CustomerRepository())

api = Blueprint("customer_api", __name__)


@api.route("/customers", methods=["POST"], endpoint="register_customer")
@swag_from({
    'tags': ['Customers'],
    'summary': 'Register a new customer',
    'description': 'Endpoint to register a new customer in the system.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'John Doe'},
                    'email': {'type': 'string', 'example': 'john.doe@example.com'},
                    'cpf': {'type': 'string', 'example': '123.456.789-10'}
                },
                'required': ['name', 'email']
            }
        }
    ],
    'responses': {
        HTTPStatus.CREATED: {
            'description': 'Customer successfully created',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'name': {'type': 'string', 'example': 'John Doe'},
                    'email': {'type': 'string', 'example': 'john.doe@example.com'},
                    'cpf': {'type': 'string', 'example': '123.456.789-10'},
                    'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                }
            }
        },
        HTTPStatus.BAD_REQUEST: {
            'description': 'Customer already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Customer already exists'}
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'Customer not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Customer not found'}
                }
            }
        }
    }
})
def register_customer():
    try:
        customer = service.create_customer(**request.json)
        output = OutputCustomerDTO.from_domain(customer=customer).to_dict()
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.BAD_REQUEST
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/customers", methods=["GET"], endpoint="list_customer")
@swag_from({
    'tags': ['Customers'],
    'summary': 'List all customers',
    'description': 'Endpoint to retrieve a list of all customers in the system.',
    'responses': {
        HTTPStatus.OK: {
            'description': 'A list of customers',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'name': {'type': 'string', 'example': 'John Doe'},
                        'cpf': {'type': 'string', 'example': '123.456.789-00'},
                        'email': {'type': 'string', 'example': 'johndoe@example.com'},
                        'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                    }
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'No customers found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'No customers found'}
                }
            }
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            'description': 'Internal server error',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'An unexpected error occurred'}
                }
            }
        }
    }
})
def list_customer():
    try:
        customers = service.all_customers()
        output = [OutputCustomerDTO.from_domain(customer=customer).to_dict() for customer in customers]
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/customers/by-cpf/<cpf>", methods=["GET"], endpoint="get_customer_by_cpf")
@swag_from({
    'tags': ['Customers'],
    'summary': 'Get customer by CPF',
    'description': 'Endpoint to retrieve a customer by their CPF.',
    'parameters': [
        {
            'name': 'cpf',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Customer CPF',
            'example': '123.456.789-10'
        }
    ],
    'responses': {
        HTTPStatus.OK: {
            'description': 'Customer found',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'name': {'type': 'string', 'example': 'John Doe'},
                    'email': {'type': 'string', 'example': 'john.doe@example.com'},
                    'cpf': {'type': 'string', 'example': '123.456.789-10'},
                    'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'Customer not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Customer not found'}
                }
            }
        }
    }
})
def get_customer_by_cpf(cpf: str):
    try:
        customer = service.find_customer_by_cpf(cpf)
        output = OutputCustomerDTO.from_domain(customer=customer).to_dict()
        return jsonify(output), HTTPStatus.OK
    except CustomerNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except CustomerAlreadyExistsException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
