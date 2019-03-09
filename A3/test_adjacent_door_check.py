from unittest import TestCase
from sud import adjacent_door_check
from unittest.mock import patch
import io
import character
import map


class TestAdjacent_door_check(TestCase):

    def test_unlock_door(self):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 4, ' L ')
        character.character_info['inventory'] = ['key']
        self.assertFalse(adjacent_door_check('unlock door'))

    def test_open_door(self):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 6, ' D ')
        self.assertFalse(adjacent_door_check('open door'))

    def test_no_key(self):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 4, ' L ')
        self.assertTrue(adjacent_door_check('unlock door'))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_key_message(self, mock_output):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 4, ' L ')
        adjacent_door_check('unlock door')
        expected_output = 'You do not have a key to open that door\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_input(self, mock_output):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 4, ' L ')
        adjacent_door_check('unlock gdfgeg')
        expected_output = 'i dont understand\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
