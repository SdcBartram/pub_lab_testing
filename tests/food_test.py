import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food1 = Food("beans on toast", 2, 1) 
        self.food2 = Food("chicken pie", 3, 1)
        self.food3 = Food("cheese pizza", 5, 1)

    def test_has_name(self):
        self.assertEqual("beans on toast", self.food1.name)

    def test_has_price(self):
        self.assertEqual(2, self.food1.price)
    
    def test_has_rejuvenation_level(self):
        self.assertEqual(1, self.food1.rejuvenation_level)
