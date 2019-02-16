from unittest import TestCase
from dungeonsanddragons import generate_consonant


class TestGenerate_consonant(TestCase):

    def test_is_a_consonant(self):
        consonants = 'bcdfghjklmnpqrstvwxz'
        self.assertTrue(generate_consonant() in consonants)

    def test_return_one_consonant(self):
        self.assertTrue(len(generate_consonant()) == 1)
