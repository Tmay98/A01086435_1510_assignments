from unittest import TestCase
from gcd import gcd


class TestGcd(TestCase):
    def test_gcd(self):
        expected = gcd(25, 10)
        actual = 5
        self.assertEqual(expected, actual)

    def test_both_negatives(self):
        expected = gcd(-25, -10)
        actual = 5
        self.assertEqual(expected, actual)

    def test_b_greater_than_a(self):
        expected = gcd(10, 25)
        actual = 5
        self.assertEqual(expected, actual)

    def test_one_negative(self):
        expected = gcd(-10, 25)
        actual = 5
        self.assertEqual(expected, actual)

    def test_one_zero(self):
        expected = gcd(0, 25)
        actual = 25
        self.assertEqual(expected, actual)
