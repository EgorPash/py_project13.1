import json


class Category:
    all_categories = 0
    all_unique_goods = 0

    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._products = []

        Category.all_categories += 1

    def add_product(self, product):
        self._products.append(product)
        Category.all_unique_goods += 1

    @property
    def products(self):
        product_list = ""
        for product in self._products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self._price = new_price
