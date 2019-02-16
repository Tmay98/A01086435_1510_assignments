from unittest import TestCase
from dungeonsanddragons import generate_name


class TestGenerate_name(TestCase):

    def test_correct_name_length(self):
        name = generate_name(5)
        self.assertTrue(len(name) == 10)
