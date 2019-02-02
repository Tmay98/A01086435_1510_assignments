from unittest import TestCase
import roman_numbers


class TestConvert_to_roman_numeral(TestCase):

    def test_convert_to_roman_numeral(self):
        self.assertEqual('V', roman_numbers.convert_to_roman_numeral(5))
