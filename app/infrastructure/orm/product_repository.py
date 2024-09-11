from typing import List, Optional, Dict
from app.infrastructure.orm.models import ProductModel

from app.domain.entities.product_entity import ProductEntity, ProductEntityFilter
from app.application.gateways.data.product_repository_Interface import ProductRepositoryInterface


class ProductRepository(ProductRepositoryInterface):

    def create(self, product_entity: ProductEntity) -> ProductEntity:
        product = ProductModel(
            name=product_entity.name,
            description=product_entity.description,
            price=product_entity.price,
            category_id=product_entity.category.id,
            created_at=product_entity.created_at
        )
        product.save()
        return ProductEntity.from_dict(data=product.model_to_dict())

    def list(self, filters: ProductEntityFilter) -> List[ProductEntity]:
        if filters.category_id:
            products = ProductModel.select().where(ProductModel.category == filters.category_id)
        else:
            products = ProductModel.select()
        return [ProductEntity.from_dict(product.model_to_dict()) for product in products]

    def get_by_id(self, product_id: int) -> Optional[ProductEntity] | None:
        product = ProductModel.get_or_none(id=product_id)
        if not product:
            return None
        return ProductEntity.from_dict(product.model_to_dict())

    def patch(self, product_id: int, fields: Dict) -> Optional[ProductEntity] | None:
        product = ProductModel.get_or_none(id=product_id)
        if not product:
            return None
        for key, value in fields.items():
            if hasattr(ProductEntity, key):
                setattr(product, key, value)
        updated_product = ProductEntity.from_dict(product.model_to_dict())
        product.save()
        return updated_product

    def delete(self, product_id: int) -> bool | None:
        product = ProductModel.delete_by_id(pk=product_id)
        if not product:
            return None
        return True
