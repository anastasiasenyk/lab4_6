

class Street:
    def __init__(self, name):
        self.name = name


class Vehicle:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description


class PublicTransport(Vehicle):
    def __init__(self, name, price):
        super(PublicTransport, self).__init__(name)
        self.price = price


class Thing:
    def __init__(self, name):
        self.name = name
