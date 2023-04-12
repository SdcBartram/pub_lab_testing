import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Frank", 100)
        
    def test_has_name(self):
        self.assertEqual("Frank", self.customer1.name)

    def test_has_wallet(self):
        self.assertEqual(100, self.customer1.wallet)
