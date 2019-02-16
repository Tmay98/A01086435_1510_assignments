from unittest import TestCase
from dungeonsanddragons import choose_inventory


class TestChoose_inventory(TestCase):
    def test_correct_length(self):
        self.assertTrue(len(choose_inventory([1, 2, 3, 4, 5, 6], 5)) == 5)

    def test_negative_selection(self):
        self.assertIsNone(choose_inventory([1, 2, 3, 4], -5))

    def test_empty_list(self):
        self.assertEqual(choose_inventory([], 0), [])

    def test_selection_too_big(self):
        self.assertIsNone(choose_inventory([1, 2, 3, 4], 7))

    def test_selection_equals_length(self):
        self.assertTrue(choose_inventory([5, 7, 3, 9, 2], 5) is not [5, 7, 3, 9, 2])
        self.assertEqual(choose_inventory([5, 7, 3, 9, 2], 5), [5, 7, 3, 9, 2])
