class Name:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            value = str(value)
        setattr(instance, self.name, value)


class Weight:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            value = int(value)
        setattr(instance, self.name, value)


class Thing:
    name = Name()
    weight = Weight()

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    __things = list()

    def __init__(self, max_weight):
        self.max_weight = max_weight

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight > self.max_weight:
            return None
        self.__things.append(thing)

    def remove_thing(self, thing):
        self.__things.remove(thing)

    def get_total_weight(self):
        return sum([thing.weight for thing in self.__things])
