from unittest import TestCase
from dungeonsanddragons import generate_syllable


class TestGenerate_syllable(TestCase):

    def test_first_letter_is_consonant(self):
        self.assertTrue(generate_syllable()[0] in 'bcdfghjklmnpqrstvwxz')

    def test_second_letter_is_vowel(self):
        self.assertTrue(generate_syllable()[1] in 'aeiouy')

    def test_length_is_2(self):
        self.assertTrue(len(generate_syllable()) == 2)
