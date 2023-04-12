class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {}

    def increase_till(self, amount):
        self.till += amount

    def increase_stock(self, amount):
        self.stock["stock_level"] += amount

    def decrease_stock(self):
        pass
