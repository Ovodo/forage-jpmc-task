import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"],
                             quote["top_ask"]["price"], (quote["top_bid"]["price"]+quote["top_ask"]["price"])/2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"],
                             quote["top_ask"]["price"], (quote["top_bid"]["price"]+quote["top_ask"]["price"])/2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_notZero(self):
        price_a = 120.48
        price_b = 0  # Setting the denominator to zero
        """ ------------ Add the assertion below ------------ """
        # The getRatio function should return None or handle this situation gracefully to prevent zero division error
        self.assertIsNone(getRatio(price_a, price_b))


if __name__ == '__main__':
    unittest.main()
