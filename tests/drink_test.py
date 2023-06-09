import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Budweiser", 12, 1)

# A Drink should have a name, and a price        # 
    def test_has_name(self):
        self.assertEqual("Budweiser", self.drink1.name)

    def test_has_price(self):
        self.assertEqual(12, self.drink1.price)

    def test_has_alcohol_level(self):
        self.assertEqual(1, self.drink1.alcohol_level)