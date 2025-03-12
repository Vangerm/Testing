class FloatValue:
    @classmethod
    def float_check(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.float_check(value)
        setattr(instance, self.name, value)


class Cell():
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet():
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)

float_value = 1.0

for i in table.cells:
    for j in i:
        j.value = float_value
        float_value += 1.0

[[print(i.__dict__) for i in j] for j in table.cells]
