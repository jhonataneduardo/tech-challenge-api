from http import HTTPStatus
from flask import Blueprint, request, jsonify

from app.adapters.driven.orm.category_repository import CategoryRepository
from app.domain.services.category_service import CategoryService

api = Blueprint("category_api", __name__)


@api.route("/categories", methods=["POST"], endpoint="register_category")
def register_category():
    service = CategoryService(CategoryRepository())
    service.create_category(**request.json)
    return jsonify({"register_category": "Ok"}), HTTPStatus.OK
