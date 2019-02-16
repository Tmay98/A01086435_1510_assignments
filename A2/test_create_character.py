from unittest import TestCase
from unittest.mock import patch
import io
import dungeonsanddragons


class TestCreate_character(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.generate_name', side_effect=['player'])
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    @patch('builtins.input', side_effect=['barbarian'])
    def test_create_character(self, mock_input, mock_roll_die, mock_generate_name, mock_stdout):
        character = dungeonsanddragons.create_character(5)
        expected_character = {'name': 'player', 'class': 'barbarian', 'HitPoints': 5, 'strength': 5, 'dexterity': 5,
                              'constitution': 5, 'intelligence': 5, 'wisdom': 5, 'charisma': 5, 'XP': 0, 'items': ''}
        self.assertEqual(character, expected_character)

    def test_wrong_input(self):
        self.assertEqual(dungeonsanddragons.create_character('wefgfwd'), None)
