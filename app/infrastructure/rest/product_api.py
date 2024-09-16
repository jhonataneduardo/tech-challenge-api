from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.infrastructure.orm.category_repository import CategoryRepository
from app.infrastructure.orm.product_repository import ProductRepository

from app.domain.exceptions import EntityNotFoundException

from app.application.usecases.product.register_product_usecase import RegisterProductUseCase
from app.application.usecases.product.list_all_products_usecase import ListAllProductsUseCase
from app.application.usecases.product.find_product_by_id_usecase import FindProductByIdUseCase
from app.application.usecases.product.update_product_usecase import UpdateProductUseCase
from app.application.usecases.product.delete_product_usecase import DeleteProductUseCase
from app.application.presenters.dtos.product_dto import OutputProductDTO

api = Blueprint("product_api", __name__)


@api.route("/products", methods=["POST"], endpoint="register_product")
@swag_from({
    'tags': ['Products'],
    'summary': 'Register a new product',
    'description': 'Endpoint to register a new product in the system.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Fanta Uva lata'},
                    'description': {'type': 'string', 'example': 'Fanta Uva lata 350ml'},
                    'price': {'type': 'number', 'format': 'float', 'example': 6.99},
                    'product_id': {'type': 'integer', 'example': 1}
                },
                'required': ['name', 'description', 'price', 'quantity', 'product_id']
            }
        }
    ],
    'responses': {
        HTTPStatus.CREATED: {
            'description': 'Product successfully created',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'name': {'type': 'string', 'example': 'Fanta Uva lata'},
                    'description': {'type': 'string', 'example': 'Fanta Uva lata 350ml'},
                    'price': {'type': 'number', 'format': 'float', 'example': 6.99},
                    'product_id': {'type': 'integer', 'example': 1},
                    'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'Category not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Category not found'}
                }
            }
        }
    }
})
def register_product():
    try:
        use_case = RegisterProductUseCase(
            product_data_provider=ProductRepository(),
            category_data_provider=CategoryRepository()
        )
        product = use_case.execute(**request.json)
        output = OutputProductDTO.from_domain(product=product).to_dict()
        return jsonify(output), HTTPStatus.CREATED
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND


@api.route("/products", methods=["GET"], endpoint="list_product")
@swag_from({
    'tags': ['Products'],
    'summary': 'List all products',
    'description': 'Endpoint to retrieve a list of all products in the system.',
    'parameters': [
        {
            'name': 'category_id',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'ID Category',
            'example': 1
        }
    ],
    'responses': {
        HTTPStatus.OK: {
            'description': 'A list of products',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'name': {'type': 'string', 'example': 'Fanta Uva lata'},
                        'description': {'type': 'string', 'example': 'Fanta Uva lata 350ml'},
                        'price': {'type': 'number', 'format': 'float', 'example': 6.99},
                        'quantity': {'type': 'integer', 'example': 10},
                        'category_id': {'type': 'integer', 'example': 1},
                        'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                    }
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'Products not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Products not found'}
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
def list_product():
    try:
        use_case = ListAllProductsUseCase(product_data_provider=ProductRepository())
        products = use_case.execute(**request.args)
        return jsonify([OutputProductDTO.from_domain(product=product).to_dict() for product in products]), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": err.args}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/products/<int:product_id>", methods=["GET"], endpoint="get_product")
def get_product(product_id: int):
    try:
        use_case = FindProductByIdUseCase(product_data_provider=ProductRepository())
        product = use_case.execute(product_id=product_id)
        output = OutputProductDTO.from_domain(product=product).to_dict()
        return jsonify(output), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/products/<product_id>", methods=["PATCH"], endpoint="patch_product")
@swag_from({
    'tags': ['Products'],
    'summary': 'Get product by ID',
    'description': 'Endpoint to retrieve a product by its ID.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'Product ID',
            'example': 1
        }
    ],
    'responses': {
        HTTPStatus.OK: {
            'description': 'Product retrieved successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'name': {'type': 'string', 'example': 'Fanta Uva lata'},
                    'description': {'type': 'string', 'example': 'Fanta Uva lata 350ml'},
                    'price': {'type': 'number', 'format': 'float', 'example': 6.99},
                    'quantity': {'type': 'integer', 'example': 10},
                    'category_id': {'type': 'integer', 'example': 1},
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
def patch_product(product_id: int):
    try:
        use_case = UpdateProductUseCase(product_data_provider=ProductRepository())
        product = use_case.execute(product_id=product_id, fields=request.json)
        output = OutputProductDTO.from_domain(product=product).to_dict()
        return jsonify(output), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/products/<product_id>", methods=["DELETE"], endpoint="delete_product")
@swag_from({
    'tags': ['Products'],
    'summary': 'Delete product by ID',
    'description': 'Endpoint to delete a product by its ID.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'Product ID',
            'example': 1
        }
    ],
    'responses': {
        HTTPStatus.NO_CONTENT: {
            'description': 'Product deleted successfully'
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
def delete_product(product_id: int):
    try:
        use_case = DeleteProductUseCase(product_data_provider=ProductRepository())
        use_case.execute(product_id=product_id)
        return jsonify(), HTTPStatus.NO_CONTENT
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
