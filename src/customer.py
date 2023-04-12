class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def check_age(self):
        return self.age >= 18
    
    def increase_drunkenness_level(self, drink):
        self.drunkenness_level += drink.alcohol_level

    def check_drunkenness_level(self):
        return self.drunkenness_level < 3

    def buy_drink(self, drink, pub):
        if self.check_age():
            if self.check_drunkenness_level():
                self.reduce_wallet(drink.price)
                pub.increase_till(drink.price)
                self.increase_drunkenness_level(drink)