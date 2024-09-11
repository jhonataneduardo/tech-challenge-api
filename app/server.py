from http import HTTPStatus
from flask import Flask, jsonify
from flasgger import Swagger

from app.infrastructure.rest import category_api, customer_api, order_api, product_api

app = Flask("FoodAPI")
swagger = Swagger(app)

BASE_PATH = "/api/v1"
app.register_blueprint(customer_api.api, url_prefix=BASE_PATH)
app.register_blueprint(category_api.api, url_prefix=BASE_PATH)
app.register_blueprint(product_api.api, url_prefix=BASE_PATH)
app.register_blueprint(order_api.api, url_prefix=BASE_PATH)

app.json.sort_keys = False


@app.get("/")
def root():
    return jsonify({"project": "Tech Challence - Fase 2"}), HTTPStatus.OK


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
