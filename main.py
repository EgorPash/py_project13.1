import json


class Category:
    name: str
    description: str
    products: list
    all_categories = 0
    all_unique_goods = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.all_unique_goods += len(set([product.name for product in products]))
        Category.all_categories += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity

    def __repr__(self):
        return f'Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})'


def load_data_from_file():
    """Загрузка данных из файла .json"""
    with open("products.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    for product in data:
        products_list = []
        for p in product['products']:
            products_list.append(Product(p['name'], p['description'], p['price'], p['quantity']))
        Category(product['name'], product['description'], products_list)
