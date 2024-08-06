import pytest
from products.main import Category, SmartPhone

@pytest.fixture
def product_1():
    return SmartPhone('топ', 'для занятия спортом', 599, 10, 'хороший', 'S-100', '128GB', 'черный')

@pytest.fixture
def product_2():
    return SmartPhone('топ2', 'для занятия спортом2', 599, 10, 'отличный', 'S-200', '256GB', 'белый')

@pytest.fixture
def category_object(product_1, product_2):
    category = Category('одежда', 'для спорта')
    category.add_product(product_1)
    category.add_product(product_2)
    return category

def test_init_category(category_object, product_1, product_2):
    assert category_object._name == 'одежда'
    assert category_object._description == 'для спорта'
    assert category_object._products == [product_1, product_2]
    assert len(category_object) == 20
    assert str(category_object) == 'одежда, количество продуктов: 20 шт.'
    assert Category.all_categories == 1