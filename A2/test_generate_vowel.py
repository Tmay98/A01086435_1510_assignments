from unittest import TestCase
from dungeonsanddragons import generate_vowel


class TestGenerate_vowel(TestCase):

    def test_is_a_vowel(self):
        vowels = 'aeiouy'
        self.assertTrue(generate_vowel() in vowels)

    def test_return_one_vowel(self):
        self.assertTrue(len(generate_vowel()) == 1)
