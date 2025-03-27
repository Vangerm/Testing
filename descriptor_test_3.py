class StringValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value, min_length=2, max_length=50):
        if not isinstance(value, str):
            value = str(value)
        if min_length <= len(value) <= max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value, max_value=10000):
        if not isinstance(value, int):
            value = int(value)
        if 0 <= value <= max_value:
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    value = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)
