from unittest import TestCase
from sud import scenario_message
from unittest.mock import patch
import io
import character
import map


class TestScenario_message(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_church_message(self, mock_output):
        character.set_column(4)
        character.set_row(9)
        scenario_message()
        expected_output = 'You come across a church that is still in good condition\n' \
                          'There is a door that seems to be unlocked\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shack_message(self, mock_output):
        character.set_column(4)
        character.set_row(7)
        scenario_message()
        expected_output = 'There is a run down shack to your left\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bridge_message(self, mock_output):
        character.set_column(8)
        character.set_row(4)
        scenario_message()
        expected_output = 'You walk over the stone bridge\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_locked_door_message(self, mock_output):
        character.set_column(6)
        character.set_row(2)
        scenario_message()
        expected_output = 'You reach the treasury but it looks like the door is locked\n' \
                          'You will need some sort of key to get through\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dirt_path_message(self, mock_output):
        character.set_column(4)
        character.set_row(6)
        scenario_message()
        expected_output = 'You are on a dirt path\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wooden_ground_message(self, mock_output):
        character.set_column(2)
        character.set_row(7)
        scenario_message()
        expected_output = 'The wooden boards creak underneath your feet\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_grass_message(self, mock_output):
        character.set_column(8)
        character.set_row(3)
        scenario_message()
        expected_output = 'You are on a grassy field\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_church_floor_message(self, mock_output):
        character.set_column(8)
        character.set_row(8)
        scenario_message()
        expected_output = 'You walk over the cold stone floor of the church\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_treasury_message(self, mock_output):
        character.set_column(3)
        character.set_row(2)
        scenario_message()
        expected_output = 'You are in the treasury\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
