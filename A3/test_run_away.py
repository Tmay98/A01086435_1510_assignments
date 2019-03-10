from unittest import TestCase
from monster import run_away
from unittest.mock import patch
import io
import character


class TestRun_away(TestCase):

    @patch('sud.roll_die', side_effect=[1, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_hit(self, mock_output, mock_roll_die):
        run_away()
        expected_output = 'The monster hits you for 1 Hitpoints as you run away\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sud.roll_die', side_effect=[5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_safely(self, mock_output, mock_roll_die):
        run_away()
        expected_output = 'You run away safely\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sud.roll_die', side_effect=[1, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_hp_decreases(self, mock_output, mock_roll_die):
        character.set_hitpoints(10)
        run_away()
        self.assertEqual(character.get_hitpoints(), 9)
