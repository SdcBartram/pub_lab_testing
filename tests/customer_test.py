import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink



class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Frank", 100)

    # A Customer should have a name, and a wallet  
    def test_has_name(self):
        self.assertEqual("Frank", self.customer1.name)

    def test_has_wallet(self):
        self.assertEqual(100, self.customer1.wallet)

    # A Customer should be able to buy a Drink from the Pub, reducing the money in its wallet and increasing the money in the Pub's till.

    def test_reduce_wallet(self):
        self.customer1.reduce_wallet(10)
        self.assertEqual(90, self.customer1.wallet)

    def test_buy_drink(self):
        drink1 = Drink("Belhaven Best", 10)
        pub1 = Pub("Red Lion", 500)
        self.customer1.buy_drink(drink1, pub1)
        self.assertEqual(90, self.customer1.wallet)
        self.assertEqual(510, pub1.till)





# Extensions:
# Add an age to the Customer. Make sure the Pub checks the age before serving the Customer.
# Add alcohol_level to the Drink, and a drunkenness level to the Customer. Every time a Customer buys a drink, the drunkenness level should go up by the alcohol_level.
# Pub should refuse service above a certain level of drunkenness!
# Advanced extensions:

# Create a Food class, that has a name, price and rejuvenation_level. Each time a Customer buys Food, their drunkenness should go down by the rejuvenation_level
# Pub can have a stock (maybe a Dictionary?) to keep track the amount of drinks available (Hard! Might need to change the drinks List to a drinks Dictionary)
# Pub can have a stock_value method to check the total value of its drinks