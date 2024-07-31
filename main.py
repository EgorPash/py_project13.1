from abc import ABC, abstractmethod

class LogMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{self.__class__.__name__}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})")


class Product(LogMixin, ABC):
    """
    Абстрактный класс "Продукт".
    Определяет базовый функционал для всех продуктов.
    """

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление продукта."""
        pass

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """Создает экземпляр продукта."""
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

    def __add__(self, other):
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Невозможно сложить товары разных типов")


class Smartphone(Product, LogMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'


class Grass(Product, LogMixin):
    def __init__(self, name, description, price, quantity, country, growth_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.growth_period = growth_period
        self.color = color

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'


class Category(LogMixin):
    all_categories = 0

    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._products = []
        Category.all_categories += 1

    @property
    def all_unique_goods(self):
        return sum(len(set([product.name for product in self._products])) for category in Category.all_categories)

    def add_product(self, product):
        if isinstance(product, Product) or issubclass(type(product), Product):
            self._products.append(product)
        else:
            raise TypeError("Невозможно добавить объект, не являющийся продуктом.")

    def __len__(self):
        return sum(product.quantity for product in self._products)

    def __str__(self):
        return f'{self._name}, количество продуктов: {len(self)} шт.'

    @property
    def products(self):
        product_list = ""
        for product in self._products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_list
