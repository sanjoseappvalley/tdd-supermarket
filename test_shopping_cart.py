import unittest
from shopping_cart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        self.product1 = 'Wine'  # 500
        self.product2 = 'BBQ Grill'  # 100
        self.product3 = 'Beer'  # 25

    def test_calculate_total_price_for_single_product(self):
        self.cart.scan(self.product2)
        self.assertEqual(self.cart.total_price(), 100)

    def test_calculate_total_price_for_multiple_products(self):
        self.cart.scan(self.product1)
        self.cart.scan(self.product2)
        self.cart.scan(self.product3)
        self.assertEqual(self.cart.total_price(), 625)

    def test_wine_no_bulk_discount(self):
        self.cart.scan(self.product1)
        self.cart.scan(self.product1)
        self.assertEqual(self.cart.total_price(), 1000)

    def test_wine_bulk_discount(self):
        self.cart.scan(self.product1)
        self.cart.scan(self.product1)
        self.cart.scan(self.product1)
        self.assertEqual(self.cart.total_price(), 1350)

    def test_beer_buy_one_get_one_free(self):
        self.cart.scan(self.product3)
        self.cart.scan(self.product3)
        self.assertEqual(self.cart.total_price(), 25)

    def test_discount_for_employees(self):
        self.cart.scan(self.product1)
        self.cart.scan(self.product2)
        self.assertEqual(self.cart.total_price(employee=True), 540)


if __name__ == "__main__":
    unittest.main()
