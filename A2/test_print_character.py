from unittest import TestCase
from unittest.mock import patch
from dungeonsanddragons import print_character
import io


class TestPrint_character(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        character = {'name': 'tommy', 'class': 'druid', 'HitPoints': 5, 'strength': 9, 'dexterity': 13,
                     'constitution': 14, 'intelligence': 9, 'wisdom': 9, 'charisma': 7, 'XP': 0, 'items': []}
        print_character(character)
        expected_output = "name tommy\nclass druid\nHitPoints 5\nstrength 9\ndexterity 13\n" \
                          "constitution 14\nintelligence 9\nwisdom 9\ncharisma 7\nXP 0\nitems []\n"
        output = mock_stdout.getvalue()
        self.assertEqual(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_input(self, mock_stdout):
        character = 15
        with self.assertRaises(AttributeError):
            print_character(character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_items(self, mock_stdout):
        character = {'name': 'tommy', 'class': 'druid', 'HitPoints': 5, 'strength': 9, 'dexterity': 13,
                     'constitution': 14, 'intelligence': 9, 'wisdom': 9, 'charisma': 7, 'XP': 0,
                     'items': ['sword', 'axe', 'bow', 'blowgun', 'staff']}
        print_character(character)
        expected_output = "name tommy\nclass druid\nHitPoints 5\nstrength 9\ndexterity 13\n" \
                          "constitution 14\nintelligence 9\nwisdom 9\ncharisma 7\nXP 0\n" \
                          "items ['sword', 'axe', 'bow', 'blowgun', 'staff']\n"
        output = mock_stdout.getvalue()
        self.assertEqual(expected_output, output)
