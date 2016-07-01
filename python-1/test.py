import unittest
import main
import time


class TestTrade(unittest.TestCase):
    def test_basic_case(self):
        stocks = [10, 7, 5, 8, 11, 9]
        self.assertTrue(main.best(stocks) == 6, "Best trade on example is 6")

    def test_longer_case(self):
        stocks = [10, 7, 11, 8, 5, 9]
        self.assertTrue(main.best(stocks) == 4, "Best trade on example is 4")

    def test_no_trade(self):
        stocks = [10, 9, 8, 7]
        self.assertTrue(main.best(stocks) == 0, "Best trade is no trade")

    def test_constant_time(self):
        stocks = range(10000000, 1, -1)
        start = time.time()
        self.assertTrue(main.best(stocks) == 0, "Best trade is no trade")
        end = time.time()

        self.assertTrue(start-end < 5, "Takes less than 5s (works in constant space and O(n) time")


if __name__ == '__main__':
    unittest.main()
