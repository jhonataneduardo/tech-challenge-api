from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from

from app.infrastructure.orm.category_repository import CategoryRepository
from app.adapters.driver.dtos.category_dto import OutputCategoryDTO

from app.domain.services.category_service import CategoryService
from app.domain.exceptions import EntityNotFoundException, EntityAlreadyExistsException

service = CategoryService(CategoryRepository())

api = Blueprint("category_api", __name__)


@api.route("/categories", methods=["POST"], endpoint="register_category")
@swag_from({
    'tags': ['Categories'],
    'summary': 'Register a new category',
    'description': 'Endpoint to register a new category in the system.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Porcões'},
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        HTTPStatus.CREATED: {
            'description': 'Category successfully created',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 5},
                    'name': {'type': 'string', 'example': 'Porcões'},
                    'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                }
            }
        },
        HTTPStatus.BAD_REQUEST: {
            'description': 'Category already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Category already exists'}
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
def register_category():
    try:
        category = service.create_category(**request.json)
        output = OutputCategoryDTO.from_domain(category=category).to_dict()
        return jsonify(output), HTTPStatus.CREATED
    except EntityAlreadyExistsException as err:
        return jsonify({"error": err.message}), HTTPStatus.BAD_REQUEST
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/categories", methods=["GET"], endpoint="list_category")
@swag_from({
    'tags': ['Categories'],
    'summary': 'List all categories',
    'description': 'Endpoint to retrieve a list of all categories in the system.',
    'responses': {
        HTTPStatus.OK: {
            'description': 'A list of categories',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 4},
                        'name': {'type': 'string', 'example': 'Porções'},
                        'created_at': {'type': 'string', 'example': '2024-05-27T09:41:42Z'}
                    }
                }
            }
        },
        HTTPStatus.NOT_FOUND: {
            'description': 'No categories found',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'No categories found'}
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
def list_category():
    try:
        categories = service.all_categories()
        output = [OutputCategoryDTO.from_domain(category=category).to_dict() for category in categories]
        return jsonify(output), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR


@api.route("/categories/<int:category_id>", methods=["GET"], endpoint="get_category")
@swag_from({
    'tags': ['Categories'],
    'summary': 'Get category by ID',
    'description': 'Endpoint to retrieve a category by its ID.',
    'parameters': [
        {
            'name': 'category_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'Category ID',
            'example': 1
        }
    ],
    'responses': {
        HTTPStatus.OK: {
            'description': 'Category retrieved successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 5},
                    'name': {'type': 'string', 'example': 'Porcões'},
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
def get_category(category_id: int):
    try:
        category = service.get_category_by_id(category_id=category_id)
        output = OutputCategoryDTO.from_domain(category=category).to_dict()
        return jsonify(output), HTTPStatus.OK
    except EntityNotFoundException as err:
        return jsonify({"error": err.message}), HTTPStatus.NOT_FOUND
    except Exception as err:
        return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
