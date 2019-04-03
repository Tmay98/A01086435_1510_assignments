from unittest import TestCase
from crud import convert_to_bool


class TestConvert_to_bool(TestCase):

    def test_convert_to_bool_True(self):
        self.assertEqual(convert_to_bool('True'), True)

    def test_convert_to_bool_Not_Capitalized(self):
        self.assertEqual(convert_to_bool('false'), False)

    def test_convert_to_bool_incorrect_input(self):
        with self.assertRaises(ValueError):
            convert_to_bool('ksdo')


