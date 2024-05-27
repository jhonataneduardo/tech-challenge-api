from app.domain.entities.product_entity import Product
from app.domain.entities.product_entity import Category


def test_simple_product_creation():
    category = Category(name="Bebidas")
    product = Product(name="Coca-cola Lata", description="Coca-cola lata 350ml", price=6.50, category=category)

    assert product.name == "Coca-cola Lata"
    assert product.description == "Coca-cola lata 350ml"
    assert product.price == 6.50
    assert product.category.name == "Bebidas"
