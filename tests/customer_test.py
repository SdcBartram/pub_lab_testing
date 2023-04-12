import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food



class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Frank", 100, 18)
        self.customer2 = Customer("Sally", 50, 16)
        self.drink1 = Drink("Belhaven Best", 10, 1)
        self.pub1 = Pub("Red Lion", 500)
        self.food1 = Food("beans on toast", 2, 1) 

    # A Customer should have a name, and a wallet  
    def test_has_name(self):
        self.assertEqual("Frank", self.customer1.name)

    def test_has_wallet(self):
        self.assertEqual(100, self.customer1.wallet)

    # A Customer should be able to buy a Drink from the Pub, reducing the money in its wallet and increasing the money in the Pub's till.

    def test_reduce_wallet(self):
        self.customer1.reduce_wallet(10)
        self.assertEqual(90, self.customer1.wallet)

    def test_check_age__pass(self):
        self.assertEqual(True, self.customer1.check_age())

    def test_check_age__fail(self):
        self.assertEqual(False, self.customer2.check_age())

    def test_increase_drunkenness_level(self):
        self.customer1.increase_drunkenness_level(self.drink1)
        self.assertEqual(1, self.customer1.drunkenness_level)

    def test_check_drunkenness_level__pass(self):
        self.assertEqual(True, self.customer2.check_drunkenness_level())

    def test_check_drunkenness_level__fail(self):
        self.customer1.buy_drink(self.drink1, self.pub1)
        self.customer1.buy_drink(self.drink1, self.pub1)
        self.customer1.buy_drink(self.drink1, self.pub1)
        self.assertEqual(False, self.customer1.check_drunkenness_level())

    def test_buy_drink_1(self):
        self.customer1.buy_drink(self.drink1, self.pub1)
        self.assertEqual(90, self.customer1.wallet)
        self.assertEqual(510, self.pub1.till)
        self.assertEqual(1,self.customer1.drunkenness_level)

    def test_buy_drink_2(self):
        self.customer2.buy_drink(self.drink1, self.pub1)
        self.assertEqual(50, self.customer2.wallet)
        self.assertEqual(500, self.pub1.till) #till increased with customer1 sale, no change shows that customer2 could not buy as underage.
        self.assertEqual(0,self.customer2.drunkenness_level)

    def test_decrease_drunkenness_level(self):
        self.customer1.buy_drink(self.drink1, self.pub1)
        self.customer1.decrease_drunkenness_level(self.food1)
        self.assertEqual(0, self.customer1.drunkenness_level)





# Extensions:
# Add an age to the Customer. Make sure the Pub checks the age before serving the Customer.
# Add alcohol_level to the Drink, and a drunkenness level to the Customer. Every time a Customer buys a drink, the drunkenness level should go up by the alcohol_level.
# Pub should refuse service above a certain level of drunkenness!
# Advanced extensions:

# Create a Food class, that has a name, price and rejuvenation_level. Each time a Customer buys Food, their drunkenness should go down by the rejuvenation_level
# Pub can have a stock (maybe a Dictionary?) to keep track the amount of drinks available (Hard! Might need to change the drinks List to a drinks Dictionary)
# Pub can have a stock_value method to check the total value of its drinks