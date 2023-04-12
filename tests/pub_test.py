import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub1 = Pub("Red Lion", 500)
        self.drink1 = Drink("Belhaven Best", 10, 1)
        self.drink2 = Drink("Guinness", 8, 1)
        self.pub1.drinks = [self.drink1, self.drink2]
        self.pub1.stock = {
            "name" : "Belhaven Best",
            "stock_level" : 5
            }
    
    # A Pub should have a name, a till, and a collection of drinks
    def test_has_name(self):
        self.assertEqual("Red Lion", self.pub1.name)

    def test_has_till(self):
        self.assertEqual(500, self.pub1.till)

    def test_has_drinks(self):
        self.assertEqual(2, len(self.pub1.drinks))

    #need to increase till amount
    def test_increase_till(self):
        self.pub1.increase_till(10)
        self.assertEqual(510, self.pub1.till)

    def test_increase_stock(self):
        self.pub1.increase_stock(1)
        self.assertEqual(6, self.pub1.stock["stock_level"])

    def test_decrease_stock(self):
        pass