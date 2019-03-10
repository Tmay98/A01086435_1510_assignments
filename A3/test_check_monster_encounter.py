from unittest import TestCase
from unittest.mock import patch
from monster import check_monster_encounter


class TestCheck_monster_encounter(TestCase):

    @patch('monster.monster_encounter', side_effect=[None])
    @patch('sud.roll_die', side_effect=[1])
    def test_monster_encounter_True(self, mock_monster_encounter, mock_roll_die):
        self.assertTrue(check_monster_encounter())

    @patch('sud.roll_die', side_effect=[5])
    def test_monster_encounter_False(self, mock_roll_die):
        self.assertFalse(check_monster_encounter())
