import unittest
import main


class EggProblem:
    def __init__(self, highest_safe_floor):
        self.highest_safe_floor = highest_safe_floor
        self.eggs_left = 2
        self.times_dropped = 0

    def drop(self, floor):
        if self.eggs_left == 0:
            return RuntimeError
        else:
            self.times_dropped += 1
            if floor > self.highest_safe_floor:
                self.eggs_left -= 1
                return True
            else:
                return False


class TestHighestSafeFloor(unittest.TestCase):
    def test_highest_safe_floor(self):
        for i in range(0, 100):
            problem = EggProblem(i)
            highest_safe_floor = main.find_floor(problem.drop)
            self.assertTrue(problem.highest_safe_floor == highest_safe_floor,
                            "Finds the highest safe floor correctly")
            self.assertTrue(problem.eggs_left >= 0,
                            "Doesn't use more than 2 eggs")
            self.assertTrue(problem.times_dropped <= 14, "Doesn't exceed worst case of 14")


if __name__ == '__main__':
    unittest.main()
