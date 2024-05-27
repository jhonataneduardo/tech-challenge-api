from app.domain.entities.category_entity import Category


def test_simple_category_creation():
    category = Category(name="Lanche")
    assert category.name == "Lanche"
