import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub1 = Pub("Red Lion", 500)
        self.drink1 = Drink("Belhaven Best", 10)
        self.drink2 = Drink("Guinness", 8)
        self.pub1.drinks = [self.drink1, self.drink2]
    
    def test_has_name(self):
        self.assertEqual("Red Lion", self.pub1.name)

    def test_has_till(self):
        self.assertEqual(500, self.pub1.till)

    def test_has_drinks(self):
        self.assertEqual(2, len(self.pub1.drinks))

    

    