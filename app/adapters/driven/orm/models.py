from typing import Dict
from datetime import datetime
from playhouse.shortcuts import model_to_dict
from peewee import (SqliteDatabase, Model, CharField, DecimalField, TextField, ForeignKeyField, DateTimeField,
                    SmallIntegerField)

db = SqliteDatabase('foodapi.db')


class CustomerModel(Model):
    name: str = CharField(max_length=120)
    email: str = CharField(max_length=80)
    cpf: str = CharField(max_length=11, unique=True)
    created_at: datetime = DateTimeField()
    updated_at: datetime = DateTimeField(null=True)

    def model_to_dict(self) -> Dict:
        return model_to_dict(self)

    class Meta:
        database = db
        table_name = "customers"


class CategoryModel(Model):
    name: str = CharField(max_length=80, unique=True)
    created_at: datetime = DateTimeField()
    updated_at: datetime = DateTimeField(null=True)

    def model_to_dict(self) -> Dict:
        return model_to_dict(self)

    class Meta:
        database = db
        table_name = "categories"


class ProductModel(Model):
    name: str = CharField(max_length=80)
    description: str = TextField()
    price: float = DecimalField()
    category: int = ForeignKeyField(CategoryModel, backref="products")
    created_at: datetime = DateTimeField()
    updated_at: datetime = DateTimeField(null=True)

    def model_to_dict(self) -> Dict:
        return model_to_dict(self)

    class Meta:
        database = db
        table_name = "products"


class OrderModel(Model):
    customer: int = ForeignKeyField(CustomerModel, backref="orders")
    status: int = SmallIntegerField()
    total: float = DecimalField()
    created_at: datetime = DateTimeField()
    updated_at: datetime = DateTimeField(null=True)

    def model_to_dict(self) -> Dict:
        return model_to_dict(self, backrefs=True)

    class Meta:
        database = db
        table_name = "orders"


class OrderItemModel(Model):
    product: int = ForeignKeyField(ProductModel)
    order: int = ForeignKeyField(OrderModel, backref="items")
    price: float = DecimalField()
    quantity: float = DecimalField()

    def model_to_dict(self) -> Dict:
        return model_to_dict(self)

    class Meta:
        database = db
        table_name = "order_items"


with db:
    db.create_tables([CustomerModel, CategoryModel, ProductModel, OrderModel, OrderItemModel])
