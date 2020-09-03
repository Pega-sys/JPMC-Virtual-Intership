import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2)



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceBEqualsZero(self):
    price_a=125.61
    price_b=0
    self.assertIsNone(getRatio(price_a, price_b))
  
  def test_getRatio_priceAEqualsZero(self):
    price_a=0
    price_b=513.25
    self.assertEqual(getRatio(price_a,price_b), 0)

  def test_getRatio_lessThanOne(self):
    price_a=259.36
    price_b=186.52
    self.assertLess(getRatio(price_a, price_b), 1)

  def test_getRatio_greaterThanOne(self):
    price_a=189.35
    price_b=75.61
    self.assertGreater(getRatio(price_a, price_b), 1) 

  def test_getRatio_exactlyOne(self):
    price_a=158.49
    price_b=158.49
    self.assertEqual(getRatio(price_a,price_b), 1)

if __name__ == '__main__':
    unittest.main()
