from unittest import TestCase
import roman_numbers


class TestConvert_to_roman_numeral(TestCase):

    def test_convert_to_roman_numeral(self):
        self.assertEqual('CMXLIV', roman_numbers.convert_to_roman_numeral(944))

    def test_lower_bound(self):
        self.assertEqual('', roman_numbers.convert_to_roman_numeral(0))

    def test_upper_bound(self):
        self.assertEqual('MMMMMMMMMM', roman_numbers.convert_to_roman_numeral(10000))
