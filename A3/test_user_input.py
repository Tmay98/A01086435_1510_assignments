from unittest import TestCase
from sud import user_input
from unittest.mock import patch
import io
import character
import map


class TestUser_input(TestCase):

    @patch('builtins.input', side_effect=['east'])
    def test_directional_input(self, mock_input):
        self.assertEqual(user_input(), 'east')

    @patch('builtins.input', side_effect=['take key'])
    def test_take_item_input(self, mock_input):
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' K ')
        self.assertEqual(user_input(), 'take key')

    @patch('builtins.input', side_effect=['open door'])
    def test_door_input(self, mock_input):
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 6, ' D ')
        self.assertEqual(user_input(), 'open door')

    @patch('builtins.input', side_effect=['help'])
    def test_help_input(self, mock_input):
        self.assertEqual(user_input(), 'help')

    @patch('builtins.input', side_effect=['use sword'])
    def test_use_item_input(self, mock_input):
        character.character_info['inventory'].append('sword')
        self.assertEqual(user_input(), 'use sword')

    @patch('builtins.input', side_effect=['quit'])
    def test_quit_input(self, mock_input):
        self.assertEqual(user_input(), 'quit')

    @patch('builtins.input', side_effect=['lbmdslm', 'east'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_input(self, mock_output, mock_input):
        user_input()
        expected_output = 'i dont understand\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
