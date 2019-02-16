from unittest import TestCase
from dungeonsanddragons import generate_vowel

class TestGenerate_vowel(TestCase):

    def test_is_a_vowel(self):
        consonants = 'aeiouy'
        self.assertTrue(generate_vowel() in consonants)

    def test_return_one_vowel(self):
        self.assertTrue(len(generate_vowel()) == 1)
