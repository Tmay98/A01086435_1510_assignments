from unittest import TestCase
from dungeonsanddragons import generate_name


class TestGenerate_name(TestCase):

    def test_correct_name_length(self):
        for i in range(20):
            name = generate_name(i)
            self.assertTrue(len(name) == (i*2))

    def test_consonant_and_verb_order(self):
        name = generate_name(20)
        verbs = 'aeiouy'
        consonants = 'bcdfghjklmnpqrstvwxz'
        for i in range(len(name)):
            if i % 2 == 1:
                self.assertIn(name[i], verbs)
            else:
                self.assertIn(name[i], consonants)

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            generate_name('ferg')

