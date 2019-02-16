from unittest import TestCase
from dungeonsanddragons import roll_die

class TestRoll_die(TestCase):
    def test_upper_bound(self):
        for i in range(100):
            self.assertTrue(roll_die(3, 6) <= 18)

    def test_lower_bound(self):
        for i in range(100):
            self.assertTrue(roll_die(3, 6) >= 3)

    def test_0_rolls(self):
        self.assertEqual(roll_die(0, 5), 0)

    def test_0_sides(self):
        self.assertEqual(roll_die(5, 0), 0)

