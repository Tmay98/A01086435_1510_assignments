from unittest import TestCase
from sum_of_primes import sum_of_primes


class TestSum_of_primes(TestCase):
    def test_sum_of_primes(self):
        expected = sum_of_primes(55)
        actual = 381
        self.assertEqual(expected, actual)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_of_primes(-20)

    def test_zero(self):
        expected = sum_of_primes(0)
        actual = 0
        self.assertEqual(expected, actual)

