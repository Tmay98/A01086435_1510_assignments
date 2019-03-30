from unittest import TestCase
from sud import print_message
from unittest.mock import patch
import io
import character
import map


class TestPrint_message(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_take_treasure_message(self, mock_output):
        map.set_map(0, 0, '  ')
        character.set_row(0)
        character.set_column(0)
        print_message('take treasure')
        expected_output = 'you accomplish your goal and retrieved the treasure\n' \
                          'now you may roam this town killing monsters as you wish\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_take_item_message(self, mock_output):
        map.set_map(0, 0, '  ')
        character.set_row(0)
        character.set_column(0)
        print_message('take bread')
        expected_output = 'you pick up bread\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_sword_message(self, mock_output):
        map.set_map(0, 0, '  ')
        character.set_row(0)
        character.set_column(0)
        print_message('use sword')
        expected_output = 'You swing your sword around looking really dumb\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_bread_message(self, mock_output):
        map.set_map(0, 0, '  ')
        character.set_row(0)
        character.set_column(0)
        print_message('use bread')
        expected_output = 'You eat the bread and return to full HP\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bread_heal(self, mock_output):
        character.set_hitpoints(5)
        print_message('use bread')
        expected_output = 'You eat the bread and return to full HP\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(character.get_hitpoints(), 10)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_open_door_message(self, mock_output):
        map.set_map(0, 0, '  ')
        character.set_row(0)
        character.set_column(0)
        print_message('open door')
        expected_output = 'you open the door\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_unlock_door_message(self, mock_output):
        map.set_map(0, 0, '  ')
        character.set_row(0)
        character.set_column(0)
        print_message('unlock door')
        expected_output = 'you unlock the door\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

