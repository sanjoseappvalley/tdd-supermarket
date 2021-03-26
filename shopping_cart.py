from collections import Counter

bulk_discount_wine_price = 450
wine_normal_price = 500
buy_one_get_one_free_beer_price = 25


class ShoppingCart:
    def __init__(self):
        self.products = []

    def scan(self, product):
        self.products.append(product)

    def total_price(self, employee=False):
        total_price = 0
        col = Counter(self.products)

        total_price += self.bulk_discounts(col, 'Wine')
        total_price += self.buy_one_get_one_free(col, 'Beer')
        total_price += col['BBQ Grill'] * 100
        if employee:
            total_price = total_price * 0.9
        return total_price

    def bulk_discounts(self, col, item):
        bulk_discount = 0

        if col[item] >= 3:
            bulk_discount = col[item] * bulk_discount_wine_price
        elif col[item]:
            bulk_discount = col[item] * wine_normal_price

        return bulk_discount

    def buy_one_get_one_free(self, col, item):
        q, r = divmod(col[item], 2)
        return (q + r) * buy_one_get_one_free_beer_price
