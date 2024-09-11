from datetime import datetime
from typing import List, Dict

from app.application.gateways.data.product_repository_Interface import ProductRepositoryInterface
from app.application.gateways.data.category_repository_interface import CategoryRepositoryInterface

from app.domain.entities.product_entity import ProductEntity, ProductEntityFilter

from app.domain.exceptions import EntityNotFoundException


class ProductService:

    def __init__(self,
                 product_repository: ProductRepositoryInterface,
                 category_repository: CategoryRepositoryInterface
                 ) -> None:
        self._product_repository = product_repository
        self._category_repository = category_repository

    def create_product(self, name: str, description: str, price: float, category_id: int) -> ProductEntity:
        category_entity = self._category_repository.get_by_id(category_id=category_id)
        if not category_entity:
            raise EntityNotFoundException("Category not found.")
        product_entity = ProductEntity(
            name=name,
            description=description,
            price=price,
            category=category_entity
        )
        return self._product_repository.create(product_entity=product_entity)

    def get_product_by_id(self, product_id: int) -> ProductEntity:
        product = self._product_repository.get_by_id(product_id=product_id)
        if not product:
            raise EntityNotFoundException("Product not found.")
        return product

    def all_products(self, **filters) -> List[ProductEntity]:
        product_filters = ProductEntityFilter(category_id=filters.get("category_id"))
        products = self._product_repository.list(filters=product_filters)
        if not products:
            raise EntityNotFoundException("No products found.")
        return products

    def patch_product(self, product_id: int, fields: Dict) -> ProductEntity:
        fields["updated_at"] = datetime.now()
        product = self._product_repository.patch(product_id=product_id, fields=fields)
        if not product:
            raise EntityNotFoundException("Product not found.")
        return product

    def delete_product_by_id(self, product_id: int) -> bool | None:
        product = self._product_repository.delete(product_id=product_id)
        if not product:
            raise EntityNotFoundException("Product not found.")
        return True
