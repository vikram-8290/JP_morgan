import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Iterate through the quotes and check if the output of getDataPoint matches the expected result
        for quote in quotes:
            with self.subTest(quote=quote):
                stock = quote['stock']
                top_bid = quote['top_bid']['price']
                top_ask = quote['top_ask']['price']
                price = (top_bid + top_ask) / 2
                expected = (stock, top_bid, top_ask, price)
                self.assertEqual(getDataPoint(quote), expected)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 117.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Iterate through the quotes and check if the output of getDataPoint matches the expected result
        for quote in quotes:
            with self.subTest(quote=quote):
                stock = quote['stock']
                top_bid = quote['top_bid']['price']
                top_ask = quote['top_ask']['price']
                price = (top_bid + top_ask) / 2
                expected = (stock, top_bid, top_ask, price)
                self.assertEqual(getDataPoint(quote), expected)

    def test_getRatio_priceBIsZero(self):
        price_a = 120.48
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b), "The ratio should be None when price_b is zero.")

    def test_getRatio_priceAIsZero(self):
        price_a = 0
        price_b = 121.68
        self.assertEqual(getRatio(price_a, price_b), 0, "The ratio should be 0 when price_a is zero.")

    def test_getRatio_normalCase(self):
        price_a = 120.48
        price_b = 121.68
        self.assertAlmostEqual(getRatio(price_a, price_b), 120.48 / 121.68, places=7, msg="The ratio should be the correct division of price_a by price_b.")

if __name__ == '__main__':
    unittest.main()
