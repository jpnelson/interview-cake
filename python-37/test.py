import unittest
import main


def is_function_random(f, sides):
    count = [0] * sides
    rolls = 100000

    for i in range(1, rolls):
        roll = f()
        count[roll - 1] += 1

    is_random = True

    for side in range(1, sides):
        is_random = is_random and abs(float(count[side]) / float(rolls) - 1.0/sides) < 0.01

    print count

    return is_random


class TestRand(unittest.TestCase):
    def test_is_rand5_random(self):
        self.assertTrue(is_function_random(main.rand5, 5), "Rand 5 function is actually random")

    def test_is_rand7_random(self):
        self.assertTrue(is_function_random(main.rand7, 7), "Rand 7 function is actually random")


if __name__ == '__main__':
    unittest.main()
