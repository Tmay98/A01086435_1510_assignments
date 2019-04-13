from unittest import TestCase
from selection_sort import selection_sort


class TestSelection_sort(TestCase):
    def test_selection_sort_with_letters(self):
        unsorted_list = ['f', 'a', 'j', 'b', 'm']
        actual = selection_sort(unsorted_list)
        expected = ['a', 'b', 'f', 'j', 'm']
        self.assertEqual(expected, actual)

    def test_selection_sort_with_numbers(self):
        unsorted_list = [25, 13, 5, 22, 1, 8, 3]
        actual = selection_sort(unsorted_list)
        expected = [1, 3, 5, 8, 13, 22, 25]
        self.assertEqual(expected, actual)

    def test_non_sortable_items_raises_error(self):
        unsorted_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(TypeError):
            selection_sort(unsorted_list)

    def test_empty_list_raises_error(self):
        unsorted_list = []
        with self.assertRaises(TypeError):
            selection_sort(unsorted_list)
