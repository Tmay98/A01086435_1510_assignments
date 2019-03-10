from unittest import TestCase
from monster import monster_encounter
from unittest.mock import patch


class TestMonster_encounter(TestCase):

    @patch('builtins.input', side_effect=['fight'])
    def test_fight_monster(self, mock_input):
        self.assertIsNone(monster_encounter())

    @patch('builtins.input', side_effect=['run away'])
    def test_run_away(self, mock_input):
        self.assertIsNone(monster_encounter())

    @patch('builtins.input', side_effect=['fefew', 'wefwefew', 'run away'])
    def test_incorrect_input_loop(self, mock_input):
        self.assertIsNone(monster_encounter())
