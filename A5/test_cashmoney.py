from unittest import TestCase
from cashmoney import cashmoney


class TestCashmoney(TestCase):
    def test_cashmoney(self):
        actual = cashmoney(265.52)
        expected = {100: 2, 50: 1, 20: 0, 10: 1, 5: 1, 2: 0, 1: 0, 0.25: 2, 0.1: 0, 0.05: 0, 0.01: 2}
        self.assertEqual(expected, actual)

    def test_zero(self):
        with self.assertRaises(ValueError):
            cashmoney(0)

    def test_negative_float(self):
        with self.assertRaises(ValueError):
            cashmoney(-5.4)
