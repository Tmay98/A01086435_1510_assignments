from unittest import TestCase
from sud import item_on_ground_message
from unittest.mock import patch
import io
import character
import map


class TestItem_on_ground_message(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_key_message(self, mock_output):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 5, ' K ')
        item_on_ground_message()
        expected_output = 'You see a key on a table\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sword_message(self, mock_output):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 5, ' S ')
        item_on_ground_message()
        expected_output = 'There is a sword propped up against the wall, it seems to be in good condition\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bread_message(self, mock_output):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 5, ' B ')
        item_on_ground_message()
        expected_output = 'You see some bread left on a bench, it looks edible\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasure_message(self, mock_output):
        character.set_row(5)
        character.set_column(5)
        map.set_map(5, 5, ' C ')
        item_on_ground_message()
        expected_output = 'You find the treasure you were searching for\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
