from unittest import TestCase
from base_conversion import base_conversion


class TestBase_conversion(TestCase):
    def test_low_to_high_base_conversion(self):
        actual = base_conversion(2, 1011, 5)
        expected = 21
        self.assertEqual(expected, actual)

    def test_high_to_low_base_conversion(self):
        actual = base_conversion(6, 43, 3)
        expected = 1000
        self.assertEqual(expected, actual)

    def test_return_is_int(self):
        actual = type(base_conversion(5, 43, 2))
        expected = int
        self.assertEqual(actual, expected)

    def test_incorrect_number(self):
        actual = base_conversion(2, 55, 7)
        expected = -1
        self.assertEqual(actual, expected)
