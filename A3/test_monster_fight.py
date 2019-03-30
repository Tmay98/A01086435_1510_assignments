from unittest import TestCase
from monster import monster_fight
from unittest.mock import patch
import io
import character


class TestMonster_fight(TestCase):

    @patch('sud.roll_die', side_effect=[5, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_player_kills_monster(self, mock_output, mock_roll_die):
        character.set_hitpoints(10)
        monster_fight()
        expected_output = 'You hit the monster for 5 Damage\nThe monster dies\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch('sud.roll_die', side_effect=[2, 5, 2, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_kills_player(self, mock_output, mock_roll_die):
        character.set_hitpoints(10)
        monster_fight()
        expected_output = 'You hit the monster for 2 Damage\nThe monster hits you for 5 Damage\n' \
                          'You hit the monster for 2 Damage\nThe monster hits you for 5 Damage\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
