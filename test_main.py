import pytest
from main import Category
from main import Smartphone

@pytest.fixture
def product1():
    return Smartphone('топ', 'для занятия спортом', 599, 10, 'хороший', 'S-100', '128GB', 'черный')

@pytest.fixture
def product2():
    return Smartphone('топ2', 'для занятия спортом2', 599, 10, 'отличный', 'S-200', '256GB', 'белый')

@pytest.fixture
def category_object(product1, product2):
    """Тест получает на вход класс Category для удобства дальнейшей работы"""
    category = Category('одежда', 'для спорта')
    category.add_product(product1)
    category.add_product(product2)
    return category

def test_init_category(category_object, product1, product2):
    """
    Тест проверяет корректность инициализации объектов класса Category.
    Также тест считает количество продуктов и категорий.
    """
    assert category_object._name == 'одежда'
    assert category_object._description == 'для спорта'
    assert category_object._products == [product1, product2]
    assert len(category_object) == 20  # сумма количества продуктов
    assert str(category_object) == 'одежда, количество продуктов: 20 шт.'
    assert Category.all_categories == 1